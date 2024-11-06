# from server.external_interface import projects_api_client
from server.database import db_connection
from server.database.models import ProjectModel


class ProjectsRepository:
    # last_id: int = 0
    # fake_db: list[dict] = []
    def __init__(self):
        self.db = db_connection.session


    def create(self, new_project_dict: dict) -> dict:
        # from datetime import datetime
        # now = datetime.now()
        # ProjectsRepository.last_id += 1
        # new_project.update(
        #     id=ProjectsRepository.last_id,
        #     created_at=now,
        #     updated_at=now,
        # )
        # ProjectsRepository.fake_db.append(new_project)
        # return new_project
        new_project = ProjectModel(**new_project_dict)
        self.db.add(new_project)
        self.db.commit()
        self.db.refresh(new_project)
        return new_project.to_dict()


    def get_list(self, limit: int, offset: int) -> list[dict]:
        # Fake DB
        # db_size = len(ProjectsRepository.fake_db)
        # first_index = min(db_size, offset)
        # last_index = min(db_size, (first_index + limit))
        # return ProjectsRepository.fake_db[first_index:last_index]

        # Fake API
        # return projects_api_client.get_list(limit, offset)  # Ejemplo de llamado a api externa

        # DB
        projects = self.db.query(ProjectModel).order_by('id').limit(limit).offset(offset).all()
        return [project.to_dict() for project in projects]

    def get_by_id(self, project_id: int) -> dict | None:
        # for project in ProjectsRepository.fake_db:
        #     if project['id'] == id:
        #         return project
        project = self.__get_one(project_id)
        if project is None: return
        return project.to_dict()
    

    def update(self, id: int, new_data: dict) -> dict | None:
        # from datetime import datetime
        # now = datetime.now()
        # current_project = self.get_by_id(id)
        # if current_project is None:
        #     return
        # current_project.update(**new_data, updated_at=now)
        # return current_project
        project = self.__get_one(id)
        if project is None: return
        for field in new_data.keys():
            setattr(project, field, new_data[field])
        self.db.commit()
        self.db.refresh(project)
        return project.to_dict()

    def delete(self, id: int) -> bool:
        # current_project = self.get_by_id(id)
        # if current_project is None:
        #     return False
        # ProjectsRepository.fake_db.remove(current_project)
        # return True
        project = self.__get_one(id)
        if project is None: return False
        self.db.delete(project)
        self.db.commit()
        return True

    def __get_one(self, project_id: int) -> ProjectModel | None:
        return self.db.query(ProjectModel).filter_by(id=project_id).first()
