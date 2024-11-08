from datetime import datetime, timedelta, timezone

import jwt

from server.configs import app_settings as settings
from server.exceptions import Unauthorized


class JwtHandler:
    def __init__(self):
        self.secret_key: str = settings.JWT_SECRET_KEY
        self.algorithm: str = settings.JWT_ALGORITHM

        self.expires_delta = timedelta(minutes=settings.JWT_EXPIRATION_TIME_MINUTES)

    def encode(self, data: dict) -> str:
        payload = data.copy()
        expire = datetime.now(timezone.utc) + self.expires_delta
        payload.update(exp=expire)
        return jwt.encode(payload, self.secret_key, self.algorithm)

    def decode(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise Unauthorized('Token expirado')
        except jwt.InvalidSignatureError:
            raise Unauthorized('Firma del token inválida')
        except jwt.InvalidTokenError:
            raise Unauthorized('Token inválido')


jwt_handler = JwtHandler()
