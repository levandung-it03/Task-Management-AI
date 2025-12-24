import pandas as pd
from app.util.constants.UserPrediction import CstFiles


def normalize(series: pd.Series):
    return (series - series.min()) / (series.max() - series.min() + 1e-6)


def split_by_user_best_task(
    df: pd.DataFrame,
    test_ratio: float = 0.1,
    min_rows_per_user: int = 5
):
    train_parts = []
    test_parts = []

    for user_id, user_df in df.groupby("user_id"):
        if len(user_df) < min_rows_per_user:
            train_parts.append(user_df)
            continue

        user_df = user_df.copy()

        # -------- heuristic quality score --------
        user_df["_quality"] = (
            user_df["is_on_time"] * 1.0
            + normalize(user_df["free_time_rto"]) * 0.5
            - normalize(user_df["used_time_rto"]) * 0.5
        )

        user_df = user_df.sort_values("_quality", ascending=False)

        n_test = max(1, int(len(user_df) * test_ratio))

        test_u = pd.concat([
            user_df.head(n_test // 2),
            user_df.tail(n_test - n_test // 2)
        ])
        train_u = user_df.iloc[n_test:]

        train_parts.append(train_u.drop(columns="_quality"))
        test_parts.append(test_u.drop(columns="_quality"))

    train_df = pd.concat(train_parts).reset_index(drop=True)
    test_df = pd.concat(test_parts).reset_index(drop=True)

    return train_df, test_df

df = pd.read_csv(CstFiles.DATA_FILE)

train_df, test_df = split_by_user_best_task(df)

data_folder = CstFiles._ROOT_STORAGE_FOLDER + CstFiles._MODEL_DATA
train_df.to_csv(data_folder + "/user_pred_train.csv", index=False)
test_df.to_csv(data_folder + "/user_pred_test.csv", index=False)

print("TRAIN domain distribution:")
print(train_df["user_domain"].value_counts())

print("\nTEST domain distribution:")
print(test_df["user_domain"].value_counts())
