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

    def to_prompt(self):
        return f"""
You are a software engineer reporting progress to your manager.
Project: {self.project}
Project description: {self.project_desc} 
Phase: {self.phase}
Phase description: {self.phase_desc}
Collection: {self.collection}
Collection description: {self.collection_desc}
Task: {self.task}
Description: {self.desc}
Report rejected times: {self.reject_count}
Reject reason: {self.reason}

Write a short formal report (3-5 sentences) starting with a greeting such as "Dear Manager" or "Dear Lead",
and ending with the name "{self.employee_name}".
"""

class ReportResponse(BaseModel):
    report: str
    success: bool
