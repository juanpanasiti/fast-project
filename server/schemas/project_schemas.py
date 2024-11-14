from datetime import datetime

from pydantic import BaseModel

from .user_schemas import UserResponse


class NewProjectRequest(BaseModel):
    title: str
    status: str = 'new'
    priority: str = 'low'
    description: str = ''


class ProjectRequest(BaseModel):
    title: str | None = None
    status: str | None = None
    priority: str | None = None
    description: str | None = None


class ProjectResponse(BaseModel):
    id: int
    title: str
    status: str = 'new'
    description: str = ''
    priority: str = ''
    user_id: int
    owner: UserResponse
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
