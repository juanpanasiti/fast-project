import logging
from typing import List

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.schemas.auth_schemas import DecodedJwt
from server.exceptions import BaseHTTPException, InternalServerError, Forbidden
from server.service import ProjectsService
from server.enums import ADMIN_ROLES


logger = logging.getLogger(__name__)


class ProjectsController:
    def __init__(self):
        self.service = ProjectsService()

    def create(self, new_project: NewProjectRequest, user_id: int) -> ProjectResponse:
        try:
            logger.debug(f'Crear proyecto {new_project.title}')
            return self.service.create(new_project, user_id)
        except BaseHTTPException as ex:
            logger.error(f'Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.create()')
            raise InternalServerError()

    def get_list(self, limit: int, offset: int, user_id: int) -> List[ProjectResponse]:
        try:
            return self.service.get_list(limit, offset, user_id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.get_list(): ' + str(ex))
            raise InternalServerError()

    def get_by_id(self, id: int, token: DecodedJwt) -> ProjectResponse:
        try:
            logger.debug(f'Buscar proyecto #{id}')
            project = self.service.get_by_id(id)
            self.__check_access(project.user_id, token)
            return project
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.get_by_id()')
            raise InternalServerError()

    def update(self, id: int, new_data: ProjectRequest, token: DecodedJwt) -> ProjectResponse:
        try:
            self.__check_access(new_data.user_id, token)
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.update()')
            raise InternalServerError()

    def delete(self, id: int, token: DecodedJwt) -> None:
        try:
            self.get_by_id(id, token)
            self.service.delete(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.delete()')
            raise InternalServerError()

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(
                f'Error en el servidor con status code {ex.status_code}: {ex.description}'
            )
        else:
            logger.error(f'Error {ex.status_code}: {ex.description}')
        raise ex

    def __check_access(self, owner_id: int, token: DecodedJwt) -> None:
        if (owner_id != token.user_id) and (token.role not in ADMIN_ROLES):
            raise Forbidden('El usuario no tiene acceso a este proyecto.')
