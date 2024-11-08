import json
import time
import logging

from fastapi import HTTPException, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint as Callback

from server.configs import app_settings as settings
from server.handlers.jwt_handler import jwt_handler


logger = logging.getLogger(__name__)


class JwtMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callback) -> Response:
        # Obtener el token que viene en el Header de la request
        token = request.headers.get('Authorization')

        # Ejecutamos la funcion del endpoint
        response = await call_next(request)

        # Trabajamos con el token
        if token is None or not token.startswith('Bearer'):
            return response

        try:
            # token -> "Bearer header.payload.signature"
            payload = jwt_handler.decode(token.split(' ')[1])

            expired_timestamp = payload['exp']
            current_timestamp = int(time.time())
            time_left: int = (expired_timestamp - current_timestamp) // 60
            if time_left < (settings.JWT_EXPIRATION_TIME_MINUTES * 0.5):
                del payload['exp']
                new_token = jwt_handler.encode(payload)
                response.headers['renewed-token'] = new_token
        except Exception as ex:
            logger.error(str(ex))

        return response
