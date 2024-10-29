import logging
from typing import List

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ProjectsService


logger = logging.getLogger(__name__)


class ProjectsController:
    def __init__(self):
        self.service = ProjectsService()

    def create(self, new_project: NewProjectRequest) -> ProjectResponse:
        try:
            logger.debug(f'Crear proyecto {new_project.title}')
            return self.service.create(new_project)
        except BaseHTTPException as ex:
            logger.error(f'Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.create()')
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[ProjectResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.get_list()')
            raise InternalServerError()

    def get_by_id(self, id: int) -> ProjectResponse:
        try:
            logger.debug(f'Buscar proyecto #{id}')
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.get_by_id()')
            raise InternalServerError()

    def update(self, id: int, new_data: ProjectRequest) -> ProjectResponse:
        try:
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.update()')
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            self.service.delete(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.delete()')
            raise InternalServerError()

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code {
                            ex.status_code}: {ex.description}')
        else:
            logger.error(f'Error {ex.status_code}: {ex.description}')
        raise ex
