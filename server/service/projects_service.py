from typing import List

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.exceptions import NotFound


class ProjectsService:
    last_id: int = 0
    fake_db: list[dict] = []

    def __init__(self):
        # TODO: instanciar repo
        pass

    def create(self, new_project: NewProjectRequest) -> ProjectResponse:
        # TODO:
        #! 1. Recibir el objeto de tipo NewProjectResponse, convertirlo a diccionario, y pasarlo a la capa de repositorio
        #! 2. Recibir del repo la respuesta (probablemente un diccionario o un objeto), convertirlo a ProjectResponse y retornarlo
        #? Codigo de ejemplo
        project_dict = self.__fake_create(new_project.model_dump())
        return ProjectResponse(**project_dict)

    def get_list(self, limit: int, offset: int) -> List[ProjectResponse]:
        # TODO:
        #! 1. Recibir los parámetros limit y offset y pasarlos a la capa repo
        #! 2. Recibir la lista de diccionarios u objetos, convertirlos a una lista de ProjectResponse y retornarlo
        #? Codigo de ejemplo
        project_list = self.__fake_get_list(limit, offset)
        return [ProjectResponse(**project) for project in project_list]

    def get_by_id(self, id: int) -> ProjectResponse:
        # TODO:
        #! 1. Recibir el id de los parámetros y pasarlo a la capa de repo
        #! 2. Recibimos el objeto o diccionario del repo, lo convertimos a un ProjectResponse y lo retornamos
        #? Codigo de ejemplo
        project = self.__fake_get_by_id(id)
        if project is None:
            raise NotFound(f'Proyecto con id #{id} no encontrado')
        return ProjectResponse(**project)

    def update(self, id: int, new_data: ProjectRequest) -> ProjectResponse:
        # TODO:
        #! 1. Recibimos los parámetros, convertimos el new_data a un diccionario y lo pasamos al repo
        #! 2. Recibimos el objeto o dict actualizado del repo, lo convertimos a ProjectResponse y lo retornamos
        #? Codigo de ejemplo
        updated_project = self.__fake_update(id, new_data.model_dump(exclude_none=True))
        if updated_project is None:
            raise NotFound(f'Proyecto con id #{id} no encontrado para actualizarse')
        return ProjectResponse(**updated_project)

    def delete(self, id: int) -> None:
        # TODO:
        #! 1. Pasamos el id al repo y retornamos
        #? Codigo de ejemplo
        if not self.__fake_delete(id):
            raise NotFound(f'Proyecto con id #{id} no encontrado para eliminarse')

    # ? FAKE METHODS
    def __fake_create(self, new_project: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        ProjectsService.last_id += 1
        new_project.update(
            id=ProjectsService.last_id,
            created_at=now,
            updated_at=now,
        )
        ProjectsService.fake_db.append(new_project)
        return new_project

    def __fake_get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(ProjectsService.fake_db)
        first_index = min(db_size, offset)
        last_index = min((db_size - first_index), limit)
        return ProjectsService.fake_db[first_index:last_index]

    def __fake_get_by_id(self, id: int) -> dict | None:
        for project in ProjectsService.fake_db:
            if project['id'] == id:
                return project

    def __fake_update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_project = self.__fake_get_by_id(id)
        if current_project is None:
            return
        current_project.update(**new_data, updated_at=now)
        return current_project

    def __fake_delete(self, id: int) -> bool:
        current_project = self.__fake_get_by_id(id)
        if current_project is None:
            return False
        ProjectsService.fake_db.remove(current_project)
        return True
