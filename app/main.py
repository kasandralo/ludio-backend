from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from app.config import settings
from app.api.routes.session import router as session_router

app = FastAPI(
    title="Ludio API",
    version="0.1.0",
    debug=settings.debug
)

class CharsetMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        if "application/json" in response.headers.get("content-type", ""):
            response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

app.add_middleware(
    CharsetMiddleware,
    allow_origins=["*"],  # 추후 도메인 지정 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(session_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Ludio API"}