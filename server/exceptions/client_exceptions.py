from .base_http_exception import BaseHTTPException


class BadRequest(BaseHTTPException):
    description = 'Algo está mal con el request enviado por el cliente.'
    status_code = 400


class Unauthorized(BaseHTTPException):
    description = 'El usuario debe estar logueado.'
    status_code = 401


class Forbidden(BaseHTTPException):
    description = 'El usuario no tiene acceso a este recurso'
    status_code = 403


class NotFound(BaseHTTPException):
    description = 'Recurso no encontrado'
    status_code = 404
