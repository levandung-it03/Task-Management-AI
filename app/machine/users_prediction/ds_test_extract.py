import pandas as pd
from sklearn.model_selection import train_test_split
from app.util.constants.UserPrediction import CstFiles

ds_csv = CstFiles.DATA_FILE
df = pd.read_csv(ds_csv)

train_parts = []
test_parts = []

for user_id, user_df in df.groupby("user_id"):
    # Nếu user quá ít data thì có thể cho hết vào train
    if len(user_df) < 5:
        train_parts.append(user_df)
        continue

    train_u, test_u = train_test_split(
        user_df,
        test_size=0.1,
        random_state=42,
        shuffle=True
    )

    train_parts.append(train_u)
    test_parts.append(test_u)

train_df = pd.concat(train_parts).reset_index(drop=True)
test_df  = pd.concat(test_parts).reset_index(drop=True)

print("TRAIN domain distribution:")
print(train_df["user_domain"].value_counts())

print("\nTEST domain distribution:")
print(test_df["user_domain"].value_counts())

data_folder = CstFiles._ROOT_STORAGE_FOLDER + CstFiles._MODEL_DATA
train_df.to_csv(data_folder + "/user_pred_train.csv", index=False)
test_df.to_csv(data_folder + "/user_pred_test.csv", index=False)
