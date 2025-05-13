from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str
    auth_provider: str  # 'google', 'apple', etc.
    created_at: datetime = Field(default_factory=datetime.utcnow)
