import numpy as np
import pandas as pd
import random

from app.dto.task_user import TaskUserRecord
from app.util.constants.UserPrediction import CstTaskConvertor, CstTask, CstUser

# Nhóm domain cho từng loại nhân sự

def create_sample_data(n_records: int = 10000, n_users: int = 1000):
    np.random.seed(42)
    user_ids = np.arange(0, n_users)

    # Mỗi user có 1 profile domain + skill base
    employee_profiles = {}
    for user_id in user_ids:
        base_skill = np.random.normal(0.6, 0.2)
        chosen_group = random.choice(CstTaskConvertor.str_domains)
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

        if is_on_time:
            # free_time bias cao (thường rảnh nhiều)
            free_time = round(np.random.beta(3, 2), 3)

            # used_time random trong khoảng hợp lệ
            used_time = round(
                np.random.uniform(0.01, max(0.01, 1.0 - free_time)),
                3
            )
        else:
            free_time = 0.0

            # used_time khi trễ: cho phép vượt deadline
            used_time = round(
                np.random.uniform(0.01, 1.95),
                3
            )

        data.append(
            {
                CstUser.user_id: user_id,
                CstTask.label_name: f"{user_id}_{CstTaskConvertor.str_domains[task_domain_idx]}",
                CstTask.domain: CstTaskConvertor.str_domains[task_domain_idx],
                CstTask.level: level,
                CstTask.priority: priority,
                CstTask.is_on_time: int(is_on_time),
                CstTask.free_time_rto: free_time,
                CstTask.used_time_rto: used_time,
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

def refactor_dataset():
    # =========================
    # CONFIG
    # =========================
    DATASET_PATH = "D:\\Develop\\My_Own_Projects\\intern_project\\fastapi\\app\\storage\\data\\user_pred_ds.csv"
    OUTPUT_PATH = "D:\\Develop\\My_Own_Projects\\intern_project\\fastapi\\app\\storage\\data\\user_pred_ds.csv"

    LATE_BUT_FAST_RATIO = 0.05  # ~5% late nhưng used_time < 1
    MAX_LATE_TIME = 1.95  # giới hạn upper bound khi nộp trễ

    np.random.seed(42)  # reproducible (optional)

    # =========================
    # LOAD DATASET
    # =========================
    df = pd.read_csv(DATASET_PATH)

    required_cols = {
        "is_on_time",
        "free_time_rto",
        "used_time_rto"
    }

    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # =========================
    # LOGIC GENERATOR
    # =========================
    def gen_used_time_rto(free_time_rto: float, is_on_time: int) -> float:
        """
        Generate used_time_rto with behavior meaning:
        - On-time:
            0 < used_time < (1 - free_time)
        - Late:
            95%: 1 < used_time < 1.95
            5% : 0 < used_time < 1  (late start / irresponsibility)
        """

        if is_on_time == 1:
            # ---- ON TIME ----
            remaining = max(0.01, 1.0 - free_time_rto)
            used_time = np.random.beta(2, 4) * remaining

        else:
            # ---- LATE ----
            if np.random.rand() < LATE_BUT_FAST_RATIO:
                # Late but fast (discipline issue)
                used_time = np.random.beta(3, 2) * 0.95
            else:
                # Late due to long execution
                used_time = np.random.uniform(1.01, MAX_LATE_TIME)

        return round(float(used_time), 3)

    # =========================
    # APPLY LOGIC
    # =========================
    df["used_time_rto"] = df.apply(
        lambda row: gen_used_time_rto(
            free_time_rto=row["free_time_rto"],
            is_on_time=row["is_on_time"]
        ),
        axis=1
    )

    # Optional but RECOMMENDED:
    # Late tasks should not have free time
    df.loc[df["is_on_time"] == 0, "free_time_rto"] = 0.0

    # =========================
    # SANITY CHECK
    # =========================
    late_df = df[df["is_on_time"] == 0]

    late_fast_ratio = (late_df["used_time_rto"] < 1).mean()
    print("Late but fast ratio:", round(late_fast_ratio, 3))

    print("\nSummary:")
    print(df[["is_on_time", "free_time_rto", "used_time_rto"]].describe())

    # =========================
    # SAVE DATASET
    # =========================
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"\n✅ Dataset saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    refactor_dataset()
