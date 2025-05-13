from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class SessionCreate(BaseModel):
    name: str
    is_public: bool = True
    description: Optional[str] = None
    created_by: UUID  # 로그인한 유저의 ID

from datetime import datetime

class SessionRead(BaseModel):
    id: UUID
    name: str
    is_public: bool
    description: Optional[str]
    created_by: UUID
    created_at: datetime
