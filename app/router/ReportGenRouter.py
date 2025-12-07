from fastapi import APIRouter

from app.dto.report_gen import ReportRequest, ReportResponse
from app.service.report_gen_svc import ReportGenSvc
from app.util.constants.Variables import Api

router = APIRouter()
PRIVATE_RPT_GEN_API_V1 = Api.API_PRIVATE_PREFIX + "/v1" + Api.API_REPORT_GEN

@router.post(PRIVATE_RPT_GEN_API_V1 + "/generate")
def generate_report_endpoint(req: ReportRequest) -> ReportResponse:
    text = ReportGenSvc.generate_report(req)
    return ReportResponse(report=text)
