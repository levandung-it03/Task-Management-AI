from pydantic import BaseModel

class ReportRequest(BaseModel):
    task: str
    desc: str
    project: str
    project_desc: str
    phase: str
    phase_desc: str
    collection: str
    collection_desc: str
    reject_count: int
    reason: str
    employee_name: str

class ReportResponse(BaseModel):
    report: str
    success: bool
