from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8000
    DEV: bool = False

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION_TIME_MINUTES: int = 60

    # External Data
    PROJECTS_API: str

    # Database
    DB_CONN: str

    # Logging
    DEBUG: bool = False

    class Config:
        env_file = '.env'
