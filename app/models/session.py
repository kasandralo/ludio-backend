from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid

class Session(SQLModel, table=True):
    __tablename__ = "sessions"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id")
    title: Optional[str]
    description: Optional[str]
    is_public: bool = True
    current_track_id: Optional[str] = Field(default=None, foreign_key="tracks.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
