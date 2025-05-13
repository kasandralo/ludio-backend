from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port: int = 8000
    debug: bool = False
    spotipy_client_id: str
    spotipy_client_secret: str
    spotipy_redirect_uri: str  # 사실상 사용하지 않는 필드
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
