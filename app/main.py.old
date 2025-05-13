from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from app.config import settings
from app.api.routes import router

app = FastAPI(debug=settings.debug)

class CharsetMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        if "application/json" in response.headers.get("content-type", ""):
            response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

app.add_middleware(CharsetMiddleware)
app.include_router(router)

# @app.get("/")
# def read_root():
#     return {
#         "message": "Ludio backend up!",
#         "debug": settings.debug,
#         "port": settings.port
#     }

# @app.get("/data")
# def get_data():
#     return {"title": "안녕하세요", "description": "FastAPI에서 한글 인코딩 테스트"}

