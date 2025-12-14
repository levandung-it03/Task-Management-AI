from fastapi import APIRouter

from app.dto.report_gen import ReportRequest, ReportResponse
from app.service.report_gen_svc import ReportGenSvc
from app.util.constants.Variables import Api

router = APIRouter()
PRIVATE_RPT_GEN_API_V1 = Api.API_PRIVATE_PREFIX + "/v1" + Api.API_REPORT_GEN

@router.post(PRIVATE_RPT_GEN_API_V1 + "/completed-report")
def generate_completed_report_endpoint(req: ReportRequest) -> ReportResponse:
    text = ReportGenSvc.generate_completed_report(req)
    return ReportResponse(report=text)

@router.post(PRIVATE_RPT_GEN_API_V1 + "/processing-report")
def generate_processing_report_endpoint(req: ReportRequest) -> ReportResponse:
    text = ReportGenSvc.generate_processing_report(req)
    return ReportResponse(report=text)

@router.post(PRIVATE_RPT_GEN_API_V1 + "/daily-report")
def generate_daily_report_endpoint(req: ReportRequest) -> ReportResponse:
    text = ReportGenSvc.generate_daily_report(req)
    return ReportResponse(report=text)
