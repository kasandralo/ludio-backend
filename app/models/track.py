from sqlmodel import SQLModel, Field
from typing import Optional

class Track(SQLModel, table=True):
    __tablename__ = "tracks"

    id: str = Field(primary_key=True)  # Use Spotify ID or hash
    title: str
    artist: str
    album: Optional[str]
    spotify_id: Optional[str]
    youtube_url: Optional[str]
    duration: Optional[int]
    bpm: Optional[float]
    metadata_json: Optional[str]
