from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8000
    DEV: bool = False

    # Logging
    DEBUG: bool = False

    class Config:
        env_file = '.env'
