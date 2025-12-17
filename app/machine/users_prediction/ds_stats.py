import pandas as pd

# =========================
# GLOBAL CONFIG (CHỈNH Ở ĐÂY)
# =========================
from app.util.constants.UserPrediction import CstFiles

DATASET_PATH = CstFiles.DATA_FILE
OUTPUT_PATH = "D:\\Develop\\My_Own_Projects\\intern_project\\fastapi\\app\\storage\\_ignored\\users_prediction\\ds_stats_result.csv"

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(DATASET_PATH)

# =========================
# BASIC CHECK
# =========================

required_cols = {
    "user_domain", "user_id", "domain", "level", "priority",
    "is_on_time", "free_time_rto", "used_time_rto"
}

missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {missing}")

# =========================
# AGGREGATION
# =========================

def summarize_user(group: pd.DataFrame) -> pd.Series:
    total_task = len(group)

    level_counts = group["level"].value_counts().to_dict()

    on_time_cnt = int((group["is_on_time"] == 1).sum())
    late_cnt = int((group["is_on_time"] == 0).sum())

    on_time_perc = round(on_time_cnt / total_task * 100, 2)
    late_perc = round(late_cnt / total_task * 100, 2)

    return pd.Series({
        "Total Task": total_task,

        "Level 0 Count": level_counts.get(0, 0),
        "Level 1 Count": level_counts.get(1, 0),
        "Level 2 Count": level_counts.get(2, 0),
        "Level 3 Count": level_counts.get(3, 0),

        "Free Time Max": round(group["free_time_rto"].max(), 3),
        "Free Time Min": round(group["free_time_rto"].min(), 3),
        "Free Time Avg": round(group["free_time_rto"].mean(), 3),

        "Used Time Max": round(group["used_time_rto"].max(), 3),
        "Used Time Min": round(group["used_time_rto"].min(), 3),
        "Used Time Avg": round(group["used_time_rto"].mean(), 3),

        "On-time Count": on_time_cnt,
        "Late Count": late_cnt,

        "On-time %": on_time_perc,
        "Late %": late_perc
    })

# =========================
# GROUP BY USER
# =========================

summary_df = (
    df
    .groupby(["domain", "user_domain", "user_id"], as_index=False)
    .apply(summarize_user)
    .reset_index(drop=True)
)

# =========================
# SORTING
# =========================

summary_df = summary_df.sort_values(
    by=["domain", "On-time %", "user_id"],
    ascending=[True, False, True]
)

# =========================
# EXPORT
# =========================

summary_df.to_csv(OUTPUT_PATH, index=False)

print("Summary generated:")
print(summary_df.head(10))
print(f"\nSaved to: {OUTPUT_PATH}")
