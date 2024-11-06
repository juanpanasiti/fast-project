from datetime import datetime

from pydantic import BaseModel

from .user_schemas import UserResponse


class NewProjectRequest(BaseModel):
    title: str
    status: str = 'new'
    description: str = ''
    user_id: int


class ProjectRequest(BaseModel):
    title: str | None = None
    status: str | None = None
    description: str | None = None
    user_id: int | None = None


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
