import os
import pandas as pd

from app.dto.task_user import TaskUserRecord, RecommendingUsersRequest, EncTskUsrPredRequest

class CstSymbols:
    UNDERLINE = "_"

class CstWeights:
    LEVEL = 5
    PRIORITY = 2.5
    IS_ON_TIME = 1
    FREE_TIME = 1
    PUNCT_SCORE = 0.5

class CstFiles:
    _ROOT_STORAGE_FOLDER = os.getcwd() + '/app/storage'
    # _ROOT_STORAGE_FOLDER = 'D:\\Develop\\My_Own_Projects\\intern_project\\fastapi\\app/storage'
    _MODEL_FOLDER = '/model'
    _MODEL_DATA = '/data'
    _LOG = '/log'

    MODEL_FILE = _ROOT_STORAGE_FOLDER + _MODEL_FOLDER + '/user_pred_recommender.pkl'
    LABEL_ENC_FILE = _ROOT_STORAGE_FOLDER + _MODEL_FOLDER + '/user_pred_label_enc.pkl'

    DATA_BACKUP_FILE = _ROOT_STORAGE_FOLDER + _MODEL_DATA + '/user_pred_ds_backup.csv'
    DATA_FILE = _ROOT_STORAGE_FOLDER + _MODEL_DATA + '/user_pred_ds.csv'
    CACHE_FILE = _ROOT_STORAGE_FOLDER + _MODEL_DATA + '/user_pred_cache.json'
    TEST_DATA_FILE = _ROOT_STORAGE_FOLDER + _MODEL_DATA + '/user_pred_test_ds.csv'

    LOG_FILE = _ROOT_STORAGE_FOLDER + _LOG + '/results.txt'


class CstErrors:
    MODEL_NOT_TRAINED = "Model hasn't been trained yet."


class CstCache:
    is_on_time = 'is_on_time'
    max_free_time = 'max_free_time'
    punct_score = 'punct_score'
    def_is_on_time = 1
    def_max_free_time = 1.0
    def_punct_score = 1.0


class CstTask:
    label_name = "user_domain"
    level = "level"
    priority = "priority"
    domain = "domain"
    is_on_time = "is_on_time"
    free_time_rto = "free_time_rto"
    late_time_perct = "late_time_perct"
    punct_score = "punct_score"


class CstUser:
    score = "score"
    user_id = "user_id"
    is_predicted_row = "is_predicted_row"


class CstModel:
    MIN_LINES_USERS_RTO = 30
    DS_TEST_SIZE = 0.2
    DS_SPLIT_RAND_STATE = 42
    REQUIRED_FEATURES = [
        CstUser.user_id,
        CstTask.domain,
        CstTask.level,
        CstTask.priority,
        CstTask.is_on_time,
        CstTask.free_time_rto,
        CstTask.punct_score
    ]
    type_category = "category"


class CstTaskConvertor:
    map_priorities = {"URGENT": 3, "HIGH": 2, "NORMAL": 1, "LOW": 0}
    enc_priorities = map_priorities.values()

    map_levels = {"HARD": 3, "ADVANCED": 2, "NORMAL": 1, "LIGHT": 0}
    enc_levels = list(map_levels.values())

    str_domains = ["BUSINESS_ANALYSIS", "BACKEND", "FRONTEND", "DEPLOY", "DESIGN", "TEST", "DOCUMENTATION",
                   "MAINTENANCE", "RESEARCH", "TRAINING", "AI"]
    map_domains = {domain: idx for idx, domain in enumerate(str_domains)}
    enc_domains = list(map_domains.values())

    @classmethod
    def encode_request(cls, request: RecommendingUsersRequest) -> EncTskUsrPredRequest:
        return EncTskUsrPredRequest(
            domain=cls.map_domains[request.domain],
            level=cls.map_levels[request.level],
            priority=cls.map_priorities[request.priority]
        )

    @classmethod
    def encode_batch(cls, batch: list[TaskUserRecord]):
        if len(batch) == 0:
            return []

        dicts = [b.dict() for b in batch]
        df = pd.DataFrame(dicts)

        df[CstTask.label_name]  = (df[CstUser.user_id].astype(str)
                                   + CstSymbols.UNDERLINE
                                   + df[CstTask.domain].astype(str))
        df[CstTask.priority]    = df[CstTask.priority].map(cls.map_priorities)
        df[CstTask.level]       = df[CstTask.level].map(cls.map_levels)
        df[CstTask.is_on_time]  = df[CstTask.is_on_time].astype(int)

        return df[[CstTask.label_name,
                   CstUser.user_id,
                   CstTask.domain,
                   CstTask.priority,
                   CstTask.level,
                   CstTask.is_on_time,
                   CstTask.free_time_rto,
                   CstTask.punct_score]]
