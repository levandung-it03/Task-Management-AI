from typing import List, Optional
from pydantic import BaseModel, Field
from app.machine.report_generator.logger import logger

class ReportResponse(BaseModel):
    success: Optional[bool] = True
    report: Optional[str] = ""
    error_message: Optional[str] = ""
class Subtask(BaseModel):
    name: Optional[str] = ""
    description: Optional[str] = ""
    status: Optional[str] = ""

class ReportRequest(BaseModel):
    project: Optional[str] = ""
    project_desc: Optional[str] = ""
    phase: Optional[str] = ""
    phase_desc: Optional[str] = ""
    collection: Optional[str] = ""
    collection_desc: Optional[str] = ""
    creator_name: Optional[str] = ""
    employee_name: Optional[str] = ""
    task_name: Optional[str] = ""
    task_desc: Optional[str] = ""
    subtask_name: Optional[str] = ""
    subtask_desc: Optional[str] = ""
    subtasks: Optional[List[Subtask]] = Field(default_factory=list)


    def to_completed_report_prompt(self):
        logger.info("to_completed_report_prompt")
        return f"""
Start with Dear Mr. of Ms. {self.creator_name}, end with {self.employee_name}\n
Generate COMPLETED_EMAIL based on the following subtask context:\n\n
Project: {self.project} ({self.project_desc})\n
Phase: {self.phase} ({self.phase_desc})\n
Collection: {self.collection} ({self.collection_desc})\n
Task: {self.task_name} ({self.task_desc})\n
f"Subtask: {self.subtask_name} ({self.subtask_desc})"
"""
        
    def to_processing_report_prompt(self):
        logger.info("to_processing_report_prompt")
        return f"""
Start with Dear Mr of Ms {self.creator_name}, end with {self.employee_name}\n
Generate IN_PROGRESS_EMAIL based on the following subtask context:\n\n
Project: {self.project} ({self.project_desc})\n
Phase: {self.phase} ({self.phase_desc})\n
Collection: {self.collection} ({self.collection_desc})\n
Task: {self.task_name} ({self.task_desc})\n
f"Subtask: {self.subtask_name} ({self.subtask_desc})"
"""

    def to_daily_report_prompt(self):
        logger.info("to_daily_report_prompt")
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
