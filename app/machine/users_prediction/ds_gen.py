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
    "junior": 3,
    "senior": 4
}

# =========================
# TASK LEVEL GENERATOR (ĐÚNG MÔ TẢ)
# =========================

def generate_task_level(user_level):
    r = random.random()

    if user_level == "senior":
        return 3 if r < random.uniform(0.15, 0.30) else 4

    if user_level == "junior":
        return 2 if r < random.uniform(0.20, 0.30) else 3

    # fresher
    return 1 if r < 0.95 else 2


# =========================
# TIME + STATUS GENERATOR (SỬA CHUẨN)
# =========================

def generate_time_and_status(priority, task_level, user_level):
    user_lv = USER_LEVEL_SCORE[user_level]

    # xác định độ khó
    if task_level < user_lv:
        difficulty = "easier"
    elif task_level == user_lv:
        difficulty = "equal"
    else:
        difficulty = "harder"

    # =========================
    # PRIORITY 1,2,3
    # =========================
    if priority in [1, 2, 3]:
        ontime_prob = {
            "equal": 0.70,
            "easier": 0.95,
            "harder": 0.30   # 70% trễ
        }
        used_range_ontime = {
            "equal": (0.15, 1.0),
            "easier": (0.15, 0.50)
        }
        used_range_late = (0.8, 3.0)

    # =========================
    # PRIORITY 4
    # =========================
    else:
        ontime_prob = {
            "equal": 0.45,
            "easier": 0.80,
            "harder": 0.10   # 90% trễ
        }
        used_range_ontime = {
            "equal": (0.50, 1.0),
            "easier": (0.30, 0.50)
        }
        used_range_late = (1.5, 3.0)

    # =========================
    # roll is_on_time
    # =========================
    is_on_time = 1 if random.random() < ontime_prob[difficulty] else 0

    # =========================
    # LATE CASE (KHÔNG PHỤ THUỘC GÌ)
    # =========================
    if is_on_time == 0:
        used_time = round(random.uniform(*used_range_late), 3)
        return 0, 0.0, used_time

    # =========================
    # ON TIME CASE
    # =========================
    free_time = round(random.uniform(0, 0.8), 3)

    min_used, max_used = used_range_ontime.get(difficulty, (0.15, 1.0))
    max_used = min(max_used, 1 - free_time)

    # nếu không thể đúng giờ → ép trễ
    if max_used < min_used:
        used_time = round(random.uniform(*used_range_late), 3)
        return 0, 0.0, used_time

    used_time = round(random.uniform(min_used, max_used), 3)
    return 1, free_time, used_time


# =========================
# DATASET GENERATION
# =========================

rows = []

for user in users:
    history_len = random.randint(50, 70)

    for _ in range(history_len):
        task_level = generate_task_level(user["user_level"])
        priority = random.randint(1, 4)

        is_on_time, free_time_rto, used_time_rto = generate_time_and_status(
            priority, task_level, user["user_level"]
        )

        rows.append({
            "user_domain": user["user_domain"],
            "user_id": user["user_id"],
            "domain": user["domain"],
            "level": task_level,
            "priority": priority,
            "is_on_time": is_on_time,
            "free_time_rto": free_time_rto,
            "used_time_rto": used_time_rto
        })

df = pd.DataFrame(rows)

# =========================
# EXPORT
# =========================

from app.util.constants.UserPrediction import CstFiles

ds_csv = CstFiles.DATA_FILE
df.to_csv(ds_csv, index=False)

print("Dataset generated:", df.shape)
