import requests
from app.machine.report_generator.config import settings
from app.machine.report_generator.logger import logger


def generate_report(task: str, desc: str, project: str, project_desc: str, 
                    phase: str, phase_desc: str, collection: str, 
                    collection_desc: str, reject_count: int, 
                    reason: str, employee_name: str) -> str:

    prompt = f"""
You are a software engineer reporting progress to your manager.
Project: {project}
Project description: {project_desc} 
Phase: {phase}
Phase description: {phase_desc}
Collection: {collection}
Collection description: {collection_desc}
Task: {task}
Description: {desc}
Report rejected times: {reject_count}
Reject reason: {reason}

Write a short formal report (3-5 sentences) starting with a greeting such as "Dear Manager" or "Dear Lead",
and ending with the name "{employee_name}".
"""

    payload = {
        "model": settings.model_name,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant generating concise work reports."},
            {"role": "user", "content": prompt}
        ],
        "temperature": settings.temperature,
        "max_tokens": settings.max_tokens
    }

    try:
        response = requests.post(settings.model_api_url, json=payload, timeout=20)
        response.raise_for_status()

        data = response.json()
        text = data["choices"][0]["message"]["content"]

        logger.info(f"Report generated successfully by model: {settings.model_name}")
        return text.strip()

    except Exception as e:
        logger.error(f"Model server error: {e}")
        raise RuntimeError("Failed to generate report from model API")
