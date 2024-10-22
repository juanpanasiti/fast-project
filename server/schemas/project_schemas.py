from datetime import datetime

from pydantic import BaseModel


class NewProjectRequest(BaseModel):
    title: str
    status: str = 'new'
    description: str = ''


class ProjectRequest(BaseModel):
    title: str | None = None
    status: str | None = None
    description: str | None = None


class ProjectResponse(BaseModel):
    id: int
    title: str
    status: str = 'new'
    description: str = ''
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
