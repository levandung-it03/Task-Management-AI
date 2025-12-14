from pydantic import BaseModel
from typing import List

class Subtask(BaseModel):
    name: str = ""
    description: str = ""
    status: str = ""

class ReportRequest(BaseModel):
    project: str = ""
    project_desc: str = ""
    phase: str = ""
    phase_desc: str = ""
    collection: str = ""
    collection_desc: str = ""
    creator_name: str = ""
    employee_name: str = ""
    task_name: str = ""
    task_desc: str = ""
    subtasks_name: str = ""
    subtasks_desc: str = ""
    subtasks: List[Subtask] = []


    def to_completed_report_prompt(self):
        return f"""
Start with Dear Mr. of Ms. {self.creator_name}, end with {self.employee_name}\n
Generate COMPLETED_EMAIL based on the following subtask context:\n\n
Project: {self.project} ({self.project_desc})\n
Phase: {self.phase} ({self.phase_desc})\n
Collection: {self.collection} ({self.collection_desc})\n
Task: {self.task_name} ({self.task_desc})\n
f"Subtask: {self.subtasks_name} ({self.subtasks_desc})"
"""
        
    def to_processing_report_prompt(self):
        return f"""
Start with Dear Mr of Ms {self.creator_name}, end with {self.employee_name}\n
Generate IN_PROGRESS_EMAIL based on the following subtask context:\n\n
Project: {self.project} ({self.project_desc})\n
Phase: {self.phase} ({self.phase_desc})\n
Collection: {self.collection} ({self.collection_desc})\n
Task: {self.task_name} ({self.task_desc})\n
f"Subtask: {self.subtasks_name} ({self.subtasks_desc})"
"""

    def to_daily_report_prompt(self):
        subtasks_info = "\n".join([
                    f"- {s.get('name', 'N/A')} - Status: {s.get('status', 'N/A')}" for s in self.subtasks
                ])
        return f"""
Generate DAILY_PROGRESS_NOTE based on the following project context:\n\n
Start with Dear Mr of Ms {self.creator_name}, end with {self.employee_name}
Project: {self.project} ({self.project_desc})\n
Phase: {self.phase} ({self.phase_desc})\n
Collection: {self.collection} ({self.collection_desc})\n
Task: {self.task_name} ({self.task_desc})\n
Subtasks Status:\n{subtasks_info}"
"""

class ReportResponse(BaseModel):
    report: str = "Can not get report from Report-Gen server"
