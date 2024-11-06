from datetime import datetime, timedelta

import jwt

from server.configs import app_settings as settings


class JwtHandler:
    def __init__(self):
        self.secret_key: str = settings.JWT_SECRET_KEY
        self.algorithm: str = settings.JWT_ALGORITHM

        self.expires_delta = timedelta(minutes=settings.JWT_EXPIRATION_TIME_MINUTE)

    def encode(self, data: dict) -> str:
        payload = data.copy()
        expire = datetime.now() + self.expires_delta
        payload.update(exp=expire)
        return jwt.encode(payload, self.secret_key, self.algorithm)
        
    def decode(self, token: str):
        pass

jwt_handler = JwtHandler()
