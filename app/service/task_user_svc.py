from app.dto.task_user import TaskUserRecord, RecommendingUsersRequest, UserPredScoreResponse
from app.machine.users_prediction.log import DebuggerSvc
from app.machine.users_prediction.model import RecModelSvc, CacheSvc, DatasetSvc


class TaskUserPredSvc:

    @classmethod
    def start_server(cls):
        RecModelSvc.start_server()

    @classmethod
    def update_model(cls, new_data: list[TaskUserRecord]) -> None:
        RecModelSvc.update_model(new_data)

    @classmethod
    def predict_top_users(cls, request: RecommendingUsersRequest) -> list[UserPredScoreResponse]:
        DebuggerSvc.start_terminal_log()
        DebuggerSvc.log_request(request)

        ranked_usr_ids_df = RecModelSvc.recommend(request)

        user_map = DebuggerSvc.get_user_map(DatasetSvc.get_dataset())
        DebuggerSvc.log_prediction(ranked_usr_ids_df, user_map, request, CacheSvc.get_cache(), 15)
        DebuggerSvc.stop_terminal_log()

        return [
            UserPredScoreResponse(user_id=row[0], score=round(row[1], 2))
            for row in ranked_usr_ids_df.itertuples(index=False)
        ]

    @classmethod
    def renew_model(cls):
        RecModelSvc.renew_model()