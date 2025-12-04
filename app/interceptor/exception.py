from fastapi.responses import JSONResponse
from fastapi import Request, FastAPI

from app.dto.api_general import ErrorResponse


class ExcHandler:
    def __init__(self, app: FastAPI):
        self.app = app

    def turn_on(self):
        @self.app.exception_handler(Exception)
        async def global_exception_handler(request: Request, exc: Exception):
            return JSONResponse(
                status_code=500,
                content=ErrorResponse(error=str(exc))
            )