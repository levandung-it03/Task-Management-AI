"""
==============INFORMATION==============
- Author: Le Van Dung (Braven) - N21DCCN021
- Date: 10/10/2025

- Required Library:
$ pip install "lightgbm~=4.0.0
$ pip install "numpy<2.0"
=======================================
"""
import os

import pandas as pd
import lightgbm as lgb
import json
import joblib

from sklearn.preprocessing import LabelEncoder
from pandas import Series

from app.dto.task_user import RecommendingUsersRequest, TaskUserRecord
from app.machine.users_prediction.log import DebuggerSvc
from app.util.constants.UserPrediction import CstTaskConvertor, CstTask, CstUser, CstFiles, CstWeights, CstModel, \
    CstCache, CstSymbols


class DatasetSvc:

    @classmethod
    def get_test_dataset(cls):
        return pd.read_csv(CstFiles.TEST_DATA_FILE)

    @classmethod
    def get_dataset(cls):
        return pd.read_csv(CstFiles.DATA_FILE)

    @classmethod
    def update_dataset(cls, new_df: pd.DataFrame):
        df = pd.read_csv(CstFiles.DATA_FILE)
        if len(new_df) == 0:
            return df
        df = pd.concat([df, new_df], ignore_index=True)

        df = df[df[CstTask.domain].isin(CstTaskConvertor.str_domains)]
        df.to_csv(CstFiles.DATA_FILE, index=False)
        return df

    @classmethod
    def rollback_dataset(cls):
        backup_df = pd.read_csv(CstFiles.DATA_BACKUP_FILE)
        backup_df.to_csv(CstFiles.DATA_FILE, index=False)

    @classmethod
    def _backup_dataset(cls, df: pd.DataFrame):
        df.to_csv(CstFiles.DATA_BACKUP_FILE, index=False)

    @classmethod
    def remove_user_data(cls, user_id: int):
        df = cls.get_dataset()
        cls._backup_dataset(df)

        df = df[df[not CstUser.user_id == user_id]]
        df.to_csv(CstFiles.DATA_FILE, index=False)


class CacheSvc:

    @classmethod
    def get_cache(cls):
        with open(CstFiles.CACHE_FILE, 'r') as f:
            return json.load(f)

    @classmethod
    def _save_cache(cls, cache: dict):
        with open(CstFiles.CACHE_FILE, 'w') as file:
            json.dump(cache, file, indent=4)

    @classmethod
    def read_cache(cls, key: str):
        cache = cls.get_cache()
        if key not in cache:
            return None
        else:
            return cache[key]

    @classmethod
    def upsert_max_value(cls, key: str, value):
        cache = cls.get_cache()
        cache[key] = max(cache[key], value)
        cls._save_cache(cache)

    @classmethod
    def upsert_key(cls, key: str, value):
        cache = cls.get_cache()
        cache[key] = value
        cls._save_cache(cache)

    @classmethod
    def init_cache(cls):
        df = pd.read_csv(CstFiles.DATA_FILE)
        cache = cls.get_cache()

        cache[CstCache.max_free_time] = max(df[CstTask.free_time_rto])
        cache[CstCache.is_on_time] = CstCache.def_is_on_time
        cache[CstCache.punct_score] = CstCache.def_punct_score

        cls._save_cache(cache)


class RecModelSvc:

    # --------Supporting----------
    @classmethod
    def pre_handle_dataset(cls, df: pd.DataFrame):
        df = df.copy().dropna()
        df.drop(labels=[
            CstUser.user_id,
            CstTask.domain
        ], axis=1, inplace=True)
        df[CstTask.level] *= CstWeights.LEVEL
        df[CstTask.priority] *= CstWeights.PRIORITY
        df[CstTask.is_on_time] *= CstWeights.IS_ON_TIME
        df[CstTask.free_time_rto] *= CstWeights.FREE_TIME
        df[CstTask.punct_score] *= CstWeights.PUNCT_SCORE
        return df

    @classmethod
    def _weights_up_row(cls, row: Series):
        row[CstTask.level] *= CstWeights.LEVEL
        row[CstTask.priority] *= CstWeights.PRIORITY
        row[CstTask.is_on_time] *= CstWeights.IS_ON_TIME
        row[CstTask.free_time_rto] *= CstWeights.FREE_TIME
        row[CstTask.punct_score] *= CstWeights.PUNCT_SCORE
        return row

    @classmethod
    def _load_encoder(cls):
        label_encoder = None
        try:
            if label_encoder is None:
                label_encoder = joblib.load(CstFiles.LABEL_ENC_FILE)
        except Exception:
            print("⚠️ Encoder not found — creating new one.")
            from sklearn.preprocessing import LabelEncoder
            label_encoder = LabelEncoder()

        return label_encoder

    @classmethod
    def _save_label_enc(cls, label_encoder: LabelEncoder):
        import joblib
        joblib.dump(label_encoder, CstFiles.LABEL_ENC_FILE)

    # -------Model Definition---------
    @classmethod
    def _init_model(cls, n_estimators=100):
        return lgb.LGBMClassifier(
            objective="multiclass",
            random_state=42,    # Model separate dataset with a fixed-size (popular in community).
            n_estimators=n_estimators,  # Num of trees.
            learning_rate=0.05,
            num_leaves=15,
            max_depth=5,
            min_data_in_leaf=5,     # From DecisionTree.
            metric="multi_logloss", # Support output score.
            verbosity=-1,           # Tur-off default log.
        )

    @classmethod
    def _save_model(cls, model: lgb.LGBMClassifier):
        joblib.dump(model, CstFiles.MODEL_FILE)

    @classmethod
    def _load_model(cls):
        model = None
        if os.path.exists(CstFiles.MODEL_FILE):
            model = joblib.load(CstFiles.MODEL_FILE)

        if model is None:
            cls.renew_model()
            model = cls._load_model()

        return model

    @classmethod
    def renew_model(cls, df: pd.DataFrame = None):
        if df is None:
            df = DatasetSvc.get_dataset()
            df = cls.pre_handle_dataset(df)

        features = df.drop(columns=[CstTask.label_name])
        labels = df[CstTask.label_name]

        label_encoder = cls._load_encoder()
        enc_labels = label_encoder.fit_transform(labels)

        model = cls._init_model()
        model.fit(features, enc_labels)

        cls._save_model(model)
        cls._save_label_enc(label_encoder)
        print("✅ Classifier trained and saved successfully.")
        return model

    @classmethod
    def update_model(cls, new_records: list[TaskUserRecord]) -> None:
        print("📈 Updating classifier model...")

        new_df = CstTaskConvertor.encode_batch(new_records)
        df = DatasetSvc.update_dataset(new_df)  # save dataset
        df = cls.pre_handle_dataset(df)

        max_free_time = max([line.free_time_rto for line in new_records])
        CacheSvc.upsert_max_value(CstCache.max_free_time, max_free_time)   # save max_free_time

        label_encoder = cls._load_encoder()
        label_encoder.fit(df[CstTask.label_name])
        cls._save_label_enc(label_encoder)    # save encoder

        features = df.drop(columns=[CstTask.label_name])
        labels = df[CstTask.label_name]

        enc_labels = label_encoder.transform(labels)

        old_model = cls._load_model()
        new_model = cls._init_model(20)
        new_model.fit(
            features,
            enc_labels,
            init_model=old_model
        )
        cls._save_model(new_model)  # save model

    @classmethod
    def pre_handle_output(cls, predictions: pd.DataFrame, request: RecommendingUsersRequest):
        result = predictions.sort_values(by=CstUser.score, ascending=False)

        result = result[
            result[CstTask.label_name].astype(str).str.endswith(f"_{request.domain}")
        ]

        # result = result.head(request.num_of_emp)  # Rely on main Backend system.
        result[CstUser.user_id] = result[CstTask.label_name].str.split(CstSymbols.UNDERLINE).str[0].astype(int)
        result[CstTask.domain] = result[CstTask.label_name].str.split(CstSymbols.UNDERLINE).str[1].astype(str)
        return result

    @classmethod
    def transform_score(cls, ranked_scores: list[float]):
        max_score = max(ranked_scores)
        min_score = min(ranked_scores)
        range_of_score = max_score - min_score
        precisions = [(score - min_score) / range_of_score * 100 for score in ranked_scores]
        return precisions

    @classmethod
    def recommend(cls, request: RecommendingUsersRequest) -> pd.DataFrame:
        model = cls._load_model()
        enc_request = CstTaskConvertor.encode_request(request)

        # -------------preparation-------------
        cached_values = CacheSvc.get_cache()
        input_df = pd.DataFrame([{
            CstTask.level: enc_request.level,
            CstTask.priority: enc_request.priority,
            CstTask.is_on_time: cached_values[CstCache.is_on_time],
            CstTask.free_time_rto: cached_values[CstCache.max_free_time],
            CstTask.punct_score: cached_values[CstCache.punct_score]
        }])
        # -------------prediction---------------
        predicted_res = model.booster_.predict(input_df, raw_score=True)
        ranked_res = cls.transform_score(predicted_res[-1])
        labels_in_order = model.classes_

        # -------------build-results--------------
        label_encoder = cls._load_encoder()
        enc_labels_in_order = label_encoder.inverse_transform(labels_in_order)

        user_predictions = []
        for label_as_idx, prob in enumerate(ranked_res):
            origin_user_domain = enc_labels_in_order[label_as_idx]
            user_predictions.append({
                CstTask.label_name: origin_user_domain,
                CstUser.score: prob
            })

        predictions = pd.DataFrame(user_predictions)
        ranked_users = cls.pre_handle_output(predictions, request)

        return ranked_users[[CstUser.user_id, CstUser.score]]

    @classmethod
    def start_server(cls):
        CacheSvc.init_cache()
        RecModelSvc.renew_model()

    @classmethod
    def run_test_loss(cls):
        RecModelSvc.start_server()
        # simulate_streaming()

        default_domain = CstTaskConvertor.str_domains[1]
        for lidx, level_str in enumerate(CstTaskConvertor.map_levels.keys()):
            for pidx, priority_str in enumerate(CstTaskConvertor.map_priorities.keys()):
                DebuggerSvc.start_terminal_log()
                print(f"\n====================== BATCH{lidx}-{pidx} ======================")
                request = RecommendingUsersRequest(
                    domain=default_domain,
                    level="NORMAL",
                    priority=priority_str
                )
                DebuggerSvc.log_request(request)
                recommendations = RecModelSvc.recommend(request)
                user_map = DebuggerSvc.get_user_map(DatasetSvc.get_dataset())
                DebuggerSvc.log_prediction(recommendations, user_map, request, CacheSvc.get_cache())
                DebuggerSvc.stop_terminal_log()

RecModelSvc.run_test_loss()