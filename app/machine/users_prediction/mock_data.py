import numpy as np
import pandas as pd
import random

from app.dto.task_user import TaskUserRecord
from app.util.constants.UserPrediction import CstTaskConvertor, CstTask, CstUser

# Nhóm domain cho từng loại nhân sự
DOMAIN_GROUPS = [
    ["BACKEND", "FRONTEND", "DEPLOY", "MAINTENANCE"],   # Dev
    ["TEST", "DOCUMENTATION"],                          # QA
    ["DESIGN", "BUSINESS_ANALYSIS"],                    # BA/Design
    ["AI", "RESEARCH", "TRAINING"],                     # AI/Research
]


def create_sample_data(n_records: int = 10000, n_users: int = 1000):
    np.random.seed(42)
    user_ids = np.arange(0, n_users)

    # Mỗi user có 1 profile domain + skill base
    employee_profiles = {}
    for user_id in user_ids:
        base_skill = np.random.normal(0.6, 0.2)
        chosen_group = random.choice(DOMAIN_GROUPS)
        employee_profiles[user_id] = {
            "base_skill": np.clip(base_skill, 0.1, 0.95),
            "domains": chosen_group,
        }

    data = []
    for _ in range(n_records):
        user_id = int(np.random.choice(user_ids))
        profile = employee_profiles[user_id]

        task_domain_str = np.random.choice(profile["domains"])
        task_domain_idx = CstTaskConvertor.map_domains[task_domain_str]

        level = np.random.randint(0, 4)
        priority = np.random.randint(0, 4)

        # Hệ số ảnh hưởng
        skill_factor = profile["base_skill"]
        task_affinity = 1.2 if task_domain_str == profile["domains"][0] else 1.0
        level_factor = 0.05 * (3 - level)  # level thấp => dễ => tốt hơn
        priority_factor = -0.05 * priority  # priority cao => stress => tệ hơn

        # Tính xác suất hoàn thành đúng hạn
        on_time_prob = 0.4 + 0.4 * skill_factor * task_affinity + level_factor + priority_factor
        on_time_prob = np.clip(on_time_prob, 0.1, 0.95)

        is_on_time = np.random.random() < on_time_prob

        # Free time & punctuality
        if is_on_time:
            free_time = round(np.random.beta(3, 2), 3)      # bias cao
            late_time = 0.0
        else:
            free_time = 0.0
            late_time = round(np.random.beta(2, 3), 3)      # bias thấp

        punctuality = round(1 - late_time, 3)

        data.append(
            {
                CstUser.user_id: user_id,
                CstTask.domain: task_domain_idx,
                CstTask.level: level,
                CstTask.priority: priority,
                CstTask.is_on_time: int(is_on_time),
                CstTask.free_time_rto: free_time,
                CstTask.punct_score: punctuality,
            }
        )

    return pd.DataFrame(data)


def save_df():
    df = create_sample_data()
    df.to_csv("sample_data.csv", index=False)
    print(f"✅ Saved {len(df)} records to sample_data.csv")


def create_fake_batch(n: int = 10) -> list[TaskUserRecord]:
    batch = []
    for _ in range(n):
        user_id = random.randint(0, 120)

        domain = random.choice(CstTaskConvertor.str_domains)
        priority = random.choice(list(CstTaskConvertor.map_priorities.keys()))
        level = random.choice(list(CstTaskConvertor.map_levels.keys()))

        is_on_time = random.random() < 0.7
        if is_on_time:
            free_time = round(random.betavariate(3, 2), 3)
            late_time = 0.0
        else:
            free_time = 0.0
            late_time = round(random.betavariate(2, 3), 3)

        record = TaskUserRecord(
            user_id=user_id,
            domain=domain,
            priority=priority,
            level=level,
            is_on_time=is_on_time,
            free_time_rto=free_time,
            punct_score=round(1 - late_time, 3),
        )
        batch.append(record)

    return batch


# if __name__ == "__main__":
#     save_df()
