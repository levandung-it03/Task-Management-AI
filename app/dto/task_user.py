from pydantic import BaseModel

class EncTskUsrPredRequest(BaseModel):
    domain: int
    priority: int
    level: int

class RecommendingUsersRequest(BaseModel):
    domain: str
    priority: str
    level: str


class TaskUserRecord(BaseModel):
    user_id: int
    domain: str
    priority: str
    level: str
    is_on_time: bool
    free_time_rto: float
    used_time_rto: float


class UpdatingTskUsrModelRequest(BaseModel):
    new_records: list[TaskUserRecord]

class UserPredScoreResponse(BaseModel):
    user_id: int
    score: float

class RecommendingUsersResponse(BaseModel):
    top_ordered_users: list[UserPredScoreResponse]
