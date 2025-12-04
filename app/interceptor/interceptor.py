from dotenv import load_dotenv
from fastapi import FastAPI, Request
from starlette.responses import Response, JSONResponse

from app.dto.api_general import ErrorResponse
from app.service.auth_svc import TmakesSpringAuthSvc
from app.util.Locale import I18n
from app.util.constants.I18n import ErrMsg
from app.util.constants.Variables import App, Api

load_dotenv()

class AuthInterceptor:
    def __init__(self, app: FastAPI):
        self.app = app

    def turn_on(self):
        @self.app.middleware(App.MIDDLEWARE_HTTP)
        async def dispatch(request: Request, call_next):
            print(f"Request: {request.method} {request.url}")
            body_bytes = await request.body()
            print(body_bytes.decode("utf-8"))
            if request.method != Api.METHOD_OPTIONS and Api.API_PRIVATE_PREFIX in request.url.path:
                key = request.headers.get(Api.HEADER_X_API_KEY)
                if not TmakesSpringAuthSvc.is_valid_authzed_api_key(key):
                    JSONResponse(
                        status_code=401,
                        content=ErrorResponse(error=I18n.get(ErrMsg.Auth.INVALID_KEY))
                    )

            # Call the next middleware or actual request handler
            response: Response = await call_next(request)
            return response
