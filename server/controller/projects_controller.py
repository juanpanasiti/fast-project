from typing import List

from fastapi import HTTPException

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.exceptions import BaseHTTPException, InternalServerError, NotFound


class ProjectsController:
    def __init__(self):
        pass  # TODO: referencia a servicio

    def create(self, new_project: NewProjectRequest) -> ProjectResponse:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # Retornar data de ejemplo
            return ProjectResponse(id=1, **new_project.model_dump())
        except BaseHTTPException as ex:
            # TODO: implementar logging
            raise ex
        except Exception:
            # TODO log: Error no contemplado en ProjectsController.create
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[ProjectResponse]:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # Codigo de ejemplo
            return []
        except BaseHTTPException as ex:
            # TODO: implementar logging
            raise ex
        except Exception:
            # TODO log: Error no contemplado en ProjectsController.create
            raise InternalServerError()

    def get_by_id(self, id: int) -> ProjectResponse:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # ejemplo de error
            raise NotFound(f'Proyecto #{id} no encontrado.')
        except BaseHTTPException as ex:
            # TODO: implementar logging
            raise ex
        except Exception:
            # TODO log: Error no contemplado en ProjectsController.create
            raise InternalServerError()

    def update(self, id: int, new_data: ProjectRequest) -> ProjectResponse:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            # ejemplo
            return ProjectResponse(id=id, **new_data.model_dump())
        except BaseHTTPException as ex:
            # TODO: implementar logging
            raise ex
        except Exception:
            # TODO log: Error no contemplado en ProjectsController.create
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            # TODO: llamar a la capa de servicio para que gestione la acción correspondiente
            return # 
        except BaseHTTPException as ex:
            # TODO: implementar logging
            raise ex
        except Exception:
            # TODO log: Error no contemplado en ProjectsController.create
            raise InternalServerError()
