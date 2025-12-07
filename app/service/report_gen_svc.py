import os

import requests
from dotenv import load_dotenv

from app.dto.report_gen import ReportRequest
from app.machine.report_generator.logger import logger
from app.util.constants.ReportGen import CstModelConfig, CstModelRes, CstLog
from app.util.constants.Variables import Env

load_dotenv()

class ReportGenSvc:
    REPORT_GEN_HOST = str(os.getenv(Env.NGROK_REPORT_GENT_HOST))

    @classmethod
    def generate_report(cls, request: ReportRequest) -> str:
        prompt = request.to_prompt()
        payload = CstModelConfig.generate_request_json(prompt)

        try:
            response = requests.post(cls.REPORT_GEN_HOST, json=payload, timeout=20)
            response.raise_for_status()

            data = response.json()
            text = data[CstModelRes.Choices][0][CstModelRes.Message][CstModelRes.Content]

            logger.info(CstLog.res_success + CstModelConfig.MODEL_NAME)
            return text.strip()

        except Exception as e:
            logger.error(CstLog.res_error + e)
            raise RuntimeError(CstLog.res_def_throw)

