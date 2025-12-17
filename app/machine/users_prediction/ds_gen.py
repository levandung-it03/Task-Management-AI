import random
import pandas as pd

random.seed(42)

# =========================
# USER SETUP
# =========================

users = []

def add_users(start, end, domain, role_ranges):
    for uid in range(start, end + 1):
        for role, (l, r) in role_ranges.items():
            if l <= uid <= r:
                users.append({
                    "user_id": uid,
                    "domain": domain,
                    "user_domain": f"{uid}__{domain}",
                    "user_level": role
                })

add_users(1, 60, "BACKEND", {
    "senior": (1, 20),
    "junior": (21, 50),
    "fresher": (51, 60)
})

add_users(61, 110, "FRONTEND", {
    "senior": (61, 75),
    "junior": (76, 105),
    "fresher": (106, 110)
})

add_users(111, 140, "TEST", {
    "senior": (111, 115),
    "junior": (116, 135),
    "fresher": (136, 140)
})

add_users(141, 145, "BUSINESS_ANALYSIS", {
    "senior": (141, 143),
    "junior": (144, 145)
})

add_users(146, 150, "HR", {
    "senior": (146, 146),
    "junior": (147, 149),
    "fresher": (150, 150)
})

USER_LEVEL_SCORE = {
    "fresher": 1,
    "junior": 2,
    "senior": 3
}

# =========================
# TASK LEVEL GENERATOR
# =========================

def generate_task_level(user_level):
    r = random.random()

    if user_level == "senior":
        return 2 if r < random.uniform(0.15, 0.30) else 3

    if user_level == "junior":
        return 2 if r < random.uniform(0.20, 0.30) else 3

    # fresher
    return random.choice([0, 1]) if r < 0.95 else 2

# =========================
# TIME + STATUS GENERATOR
# =========================

def generate_time_and_status(priority, task_level, user_level):
    user_lv = USER_LEVEL_SCORE[user_level]

    if task_level < user_lv:
        difficulty = "easier"
    elif task_level == user_lv:
        difficulty = "equal"
    else:
        difficulty = "harder"

    # -------- probability --------
    if priority in [0, 1, 3]:
        prob_map = {
            "equal": 0.70,
            "easier": 0.95,
            "harder": 0.30
        }
        used_min_map = {
            "equal": 0.15,
            "easier": 0.15,
            "harder": 0.80
        }
    else:  # priority == 2
        prob_map = {
            "equal": 0.45,
            "easier": 0.80,
            "harder": 0.10
        }
        used_min_map = {
            "equal": 0.50,
            "easier": 0.30,
            "harder": 1.50
        }

    # roll on-time first
    want_on_time = random.random() < prob_map[difficulty]

    # -------- late --------
    if not want_on_time:
        return 0, 0.0, round(random.uniform(0, 3), 3)

    # -------- attempt on time --------
    free_time = round(random.uniform(0.01, 0.8), 3)
    used_min = used_min_map[difficulty]
    remaining = 1 - free_time

    # 🚨 PHYSICAL IMPOSSIBILITY CHECK
    if used_min > remaining:
        # impossible to be on time -> force late
        return 0, 0.0, round(random.uniform(used_min, 3), 3)

    used_time = round(random.uniform(used_min, remaining), 3)
    return 1, free_time, used_time

# =========================
# DATASET GENERATION
# =========================

rows = []

for user in users:
    history_len = random.randint(50, 70)

    for _ in range(history_len):
        task_level = generate_task_level(user["user_level"])
        priority = random.randint(0, 3)

        is_on_time, free_time, used_time = generate_time_and_status(
            priority, task_level, user["user_level"]
        )

        rows.append({
            "user_domain": user["user_domain"],
            "user_id": user["user_id"],
            "domain": user["domain"],
            "level": task_level,
            "priority": priority,
            "is_on_time": is_on_time,
            "free_time_rto": free_time,
            "used_time_rto": used_time
        })

df = pd.DataFrame(rows)

# =========================
# EXPORT
# =========================
from app.util.constants.UserPrediction import CstFiles

ds_csv = CstFiles.DATA_FILE
df.to_csv(ds_csv,index=False)

print("Dataset generated:", df.shape)
