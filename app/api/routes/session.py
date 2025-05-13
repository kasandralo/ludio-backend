from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4
from app.schemas.session import SessionCreate, SessionRead
from app.models.session import Session
from app.core.database import async_session
from sqlmodel import select

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/sessions", response_model=SessionRead)
async def create_session(session_data: SessionCreate, db: AsyncSession = Depends(get_db)):
    new_session = Session(
        id=uuid4(),
        name=session_data.name,
        is_public=session_data.is_public,
        description=session_data.description,
        created_by=session_data.created_by,
    )

    db.add(new_session)
    await db.commit()
    await db.refresh(new_session)

    return new_session

