import pandas as pd

# =========================
# LOAD DATA
# =========================

from app.util.constants.UserPrediction import CstFiles

ds_csv = CstFiles.DATA_FILE
df = pd.read_csv(ds_csv)

# =========================
# CONSTANTS
# =========================

USER_LEVEL_SCORE = {
    "fresher": 1,
    "junior": 2,
    "senior": 3
}


# =========================
# HARD CONSTRAINT CHECKS
# =========================

def check_hard_constraints(df):
    errors = []

    bad = df[(df.is_on_time == 0) & (df.free_time_rto != 0)]
    if not bad.empty:
        errors.append(f"❌ is_on_time=0 but free_time_rto != 0 ({len(bad)})")

    bad = df[(df.is_on_time == 1) & ((df.free_time_rto + df.used_time_rto) > 1.001)]
    if not bad.empty:
        errors.append(f"❌ is_on_time=1 but free+used > 1 ({len(bad)})")

    bad = df[~df.level.between(1, 4)]
    if not bad.empty:
        errors.append("❌ level out of [1,4]")

    bad = df[~df.priority.between(1, 4)]
    if not bad.empty:
        errors.append("❌ priority out of [1,4]")

    bad = df[~df.free_time_rto.between(0, 0.8)]
    if not bad.empty:
        errors.append("❌ free_time_rto out of [0,0.8]")

    bad = df[~df.used_time_rto.between(0, 3)]
    if not bad.empty:
        errors.append("❌ used_time_rto out of [0,3]")
        # =========================
        # NEW CHECKS
        # =========================

        # ---- delayed_time_rto basic range ----
        bad = df[df.delayed_time_rto < 0.05]
        if not bad.empty:
            errors.append(f"❌ delayed_time_rto < 0.05 ({len(bad)})")

        # ---- on-time: free + used + delayed <= 1 ----
        bad = df[
            (df.is_on_time == 1) &
            ((df.free_time_rto + df.used_time_rto + df.delayed_time_rto) > 1.001)
            ]
        if not bad.empty:
            errors.append(
                f"❌ is_on_time=1 but free+used+delayed > 1 ({len(bad)})"
            )

        # ---- late: delayed_time_rto in [0.05, 1.8] ----
        bad = df[
            (df.is_on_time == 0) &
            (~df.delayed_time_rto.between(0.05, 1.8))
            ]
        if not bad.empty:
            errors.append(
                f"❌ is_on_time=0 but delayed_time_rto not in [0.05,1.8] ({len(bad)})"
            )

        # ---- free_time_scr correctness ----
        bad = df[
            (df.free_time_scr - df.free_time_rto * df.priority).abs() > eps
            ]
        if not bad.empty:
            errors.append(
                f"❌ free_time_scr != free_time_rto * priority ({len(bad)})"
            )

        # ---- bad_time_scr correctness ----
        bad = df[
            (df.bad_time_scr - df.delayed_time_rto * df.priority).abs() > eps
            ]
        if not bad.empty:
            errors.append(
                f"❌ bad_time_scr != delayed_time_rto * priority ({len(bad)})"
            )

    return errors


# =========================
# USER LEVEL INFERENCE
# =========================

def infer_user_level(user_id, domain):
    if domain == "BACKEND":
        if 1 <= user_id <= 20:
            return "senior"
        if 21 <= user_id <= 50:
            return "junior"
        return "fresher"

    if domain == "FRONTEND":
        if 61 <= user_id <= 75:
            return "senior"
        if 76 <= user_id <= 105:
            return "junior"
        return "fresher"

    if domain == "TEST":
        if 111 <= user_id <= 115:
            return "senior"
        if 116 <= user_id <= 135:
            return "junior"
        return "fresher"

    if domain == "BUSINESS_ANALYSIS":
        if 141 <= user_id <= 143:
            return "senior"
        return "junior"

    if domain == "HR":
        if user_id == 146:
            return "senior"
        if 147 <= user_id <= 149:
            return "junior"
        return "fresher"

    raise ValueError(f"Unknown user: {user_id}, {domain}")


# =========================
# DERIVE DIFFICULTY
# =========================

def derive_difficulty(row):
    user_level = infer_user_level(row.user_id, row.domain)
    user_lv = USER_LEVEL_SCORE[user_level]

    if row.level < user_lv:
        return "easier"
    if row.level == user_lv:
        return "equal"
    return "harder"


df["difficulty"] = df.apply(derive_difficulty, axis=1)

# infer user_level once for statistical checks
df["user_level_inferred"] = df.apply(
    lambda r: infer_user_level(r.user_id, r.domain),
    axis=1
)


# =========================
# STATISTICAL LOGIC CHECKS
# =========================

def check_statistical_logic(df):
    report = {}

    # late rate by difficulty
    for diff in ["easier", "equal", "harder"]:
        sub = df[df.difficulty == diff]
        report[f"{diff}_late_rate"] = round(1 - sub.is_on_time.mean(), 4)

    # late rate by priority
    prio_late = 1 - df.groupby("priority").is_on_time.mean()
    report["late_rate_by_priority"] = prio_late.round(4).to_dict()

    # fresher should rarely do hard tasks
    fresher = df[df.user_level_inferred == "fresher"]
    report["fresher_hard_task_ratio"] = round(
        (fresher.level >= 2).mean(), 4
    )

    return report


# =========================
# RUN CHECKER
# =========================

hard_errors = check_hard_constraints(df)

print("\n===== HARD CONSTRAINT CHECK =====")
if not hard_errors:
    print("✅ PASSED: No hard logic violation")
else:
    for e in hard_errors:
        print(e)

print("\n===== STATISTICAL LOGIC CHECK =====")
stats = check_statistical_logic(df)
for k, v in stats.items():
    print(f"{k}: {v}")
