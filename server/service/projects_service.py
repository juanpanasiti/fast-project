from typing import List

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.exceptions import NotFound
from server.repository import ProjectsRepository


class ProjectsService:

    def __init__(self):
        self.project_repo = ProjectsRepository()

    def create(self, new_project: NewProjectRequest) -> ProjectResponse:
        project_dict = self.project_repo.create(new_project.model_dump())
        return ProjectResponse(**project_dict)

    def get_list(self, limit: int, offset: int) -> List[ProjectResponse]:
        project_list = self.project_repo.get_list(limit, offset)
        return [ProjectResponse(**project) for project in project_list]

    def get_by_id(self, id: int) -> ProjectResponse:
        project = self.project_repo.get_by_id(id)
        if project is None:
            raise NotFound(f'Proyecto con id #{id} no encontrado')
        return ProjectResponse(**project)

    def update(self, id: int, new_data: ProjectRequest) -> ProjectResponse:
        updated_project = self.project_repo.update(
            id, new_data.model_dump(exclude_none=True))
        if updated_project is None:
            raise NotFound(f'Proyecto con id #{
                           id} no encontrado para actualizarse')
        return ProjectResponse(**updated_project)

    def delete(self, id: int) -> None:
        if not self.project_repo.delete(id):
            raise NotFound(f'Proyecto con id #{
                           id} no encontrado para eliminarse')
