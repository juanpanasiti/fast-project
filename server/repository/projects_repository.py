

class ProjectsRepository:
    last_id: int = 0
    fake_db: list[dict] = []

    def create(self, new_project: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        ProjectsRepository.last_id += 1
        new_project.update(
            id=ProjectsRepository.last_id,
            created_at=now,
            updated_at=now,
        )
        ProjectsRepository.fake_db.append(new_project)
        return new_project

    def get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(ProjectsRepository.fake_db)
        first_index = min(db_size, offset)
        last_index = min(db_size, (first_index + limit))
        return ProjectsRepository.fake_db[first_index:last_index]

    def get_by_id(self, id: int) -> dict | None:
        for project in ProjectsRepository.fake_db:
            if project['id'] == id:
                return project

    def update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_project = self.get_by_id(id)
        if current_project is None:
            return
        current_project.update(**new_data, updated_at=now)
        return current_project

    def delete(self, id: int) -> bool:
        current_project = self.get_by_id(id)
        if current_project is None:
            return False
        ProjectsRepository.fake_db.remove(current_project)
        return True
