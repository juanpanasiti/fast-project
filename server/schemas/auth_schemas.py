from datetime import datetime

from pydantic import BaseModel, EmailStr

from .user_schemas import UserResponse
from server.enums import RoleEnum


class RegisterUser(BaseModel):
    username: str
    password: str
    email: EmailStr
    role: RoleEnum = RoleEnum.COMMON


class LoginUser(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str = ''
    token_type: str = 'bearer'
    user: UserResponse


class DecodedJwt(BaseModel):
    user_id: int
    role: RoleEnum
    exp: datetime
