from fastapi import APIRouter

from app.dto.task_user import UpdatingTskUsrModelRequest, RecommendingUsersRequest, RecommendingUsersResponse
from app.service.task_user_svc import TaskUserPredSvc
from app.util.constants.Variables import Api

router = APIRouter()
PRIVATE_TSK_USR_API_V1 = Api.API_PRIVATE_PREFIX + "/v1" + Api.API_TASK_USER

@router.put(PRIVATE_TSK_USR_API_V1 + "/update-model")
def update_model_by_records(request: UpdatingTskUsrModelRequest):
    TaskUserPredSvc.update_model(request.new_records)
    return None

@router.put(PRIVATE_TSK_USR_API_V1 + "/renew-model")
def renew_model():
    TaskUserPredSvc.renew_model()
    return None

@router.post(PRIVATE_TSK_USR_API_V1 + "/recommend-users")
def recommend_users(request: RecommendingUsersRequest) -> RecommendingUsersResponse:
    return RecommendingUsersResponse(top_ordered_users=TaskUserPredSvc.predict_top_users(request))