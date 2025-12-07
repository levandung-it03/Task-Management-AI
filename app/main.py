import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.interceptor.exception import ExcHandler
from app.interceptor.interceptor import AuthInterceptor
from app.router import TaskUserPredRouter, ReportGenRouter
from app.service.task_user_svc import TaskUserPredSvc
from app.util.constants.Variables import Env

from app.dto.report_gen import ReportRequest, ReportResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    TaskUserPredSvc.start_server()
    yield

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}}, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv(Env.SPRING_TMAKES_HOST)],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

exceptionHandler = ExcHandler(app)
exceptionHandler.turn_on()

# authInterceptor = AuthInterceptor(app)
# authInterceptor.turn_on()

# Include routers
app.include_router(TaskUserPredRouter.router)
app.include_router(ReportGenRouter.router)