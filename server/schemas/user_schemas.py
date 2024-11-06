from datetime import datetime

from pydantic import BaseModel, EmailStr

from server.enums import RoleEnum


class NewUserRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    role: RoleEnum = RoleEnum.COMMON


class UserRequest(BaseModel):
    username: str | None = None
    password: str | None = None
    email: EmailStr | None = None
    role: RoleEnum | None = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    class Config:
        from_attributes = True
