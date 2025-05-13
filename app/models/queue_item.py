from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class QueueItem(SQLModel, table=True):
    __tablename__ = "queue_items"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    session_id: uuid.UUID = Field(foreign_key="sessions.id")
    track_id: str = Field(foreign_key="tracks.id")
    position: int
    added_by_user_id: Optional[uuid.UUID] = Field(default=None, foreign_key="users.id")
    added_at: datetime = Field(default_factory=datetime.utcnow)
