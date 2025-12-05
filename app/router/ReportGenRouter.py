from fastapi import APIRouter

from app.machine.report_generator.config import Settings
from app.dto.report_gen import ReportRequest, ReportResponse
from app.service.report_gen_svc import generate_report
from app.util.constants.Variables import Api

router = APIRouter()
PRIVATE_RPT_GEN_API_V1 = Api.API_PRIVATE_PREFIX + "/v1" + Api.API_REPORT_GEN

@router.post(PRIVATE_RPT_GEN_API_V1 + "/generate", response_model=ReportResponse)
def generate_report_endpoint(req: ReportRequest):

    text = generate_report(
        task=req.task,
        desc=req.desc,
        project=req.project,
        project_desc=req.project_desc,
        phase=req.phase,
        phase_desc=req.phase_desc,
        collection=req.collection,
        collection_desc=req.collection_desc,
        reject_count=req.reject_count,
        reason=req.reason,
        employee_name=req.employee_name
    )

    return ReportResponse(report=text)
