import logging

from server.repository import UsersRepository
from server.exceptions import BadRequest
from server.schemas.auth_schemas import RegisterUser, LoginUser, TokenResponse
from server.schemas.user_schemas import UserResponse, NewUserRequest
from .users_service import UsersService
from server.handlers.jwt_handler import jwt_handler
from server.enums import RoleEnum as Role

logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self):
        self.user_service = UsersService()
        self.user_repo = UsersRepository()

    def register(self, new_user: RegisterUser) -> TokenResponse:
        new_user_dict = new_user.model_dump()
        new_user_dict.update(role=Role.COMMON)
        user = self.user_service.create(NewUserRequest(**new_user_dict))
        return self.__get_token(user)

    def login(self, credentials: LoginUser) -> TokenResponse:
        user = self.user_repo.get_by_username(credentials.username)
        if user is None:
            raise BadRequest('Error en username/password')
        is_pass_ok = self.user_repo.check_password(user['id'], credentials.password)
        if not is_pass_ok:
            raise BadRequest('Error en username/password')
        response = TokenResponse.model_validate({'user': user})
        response.access_token = self.__get_user_token(response.user.id, response.user.role)
        return response

    def __get_token(self, user: UserResponse) -> TokenResponse:
        token = self.__get_user_token(user.id, user.role)
        return TokenResponse(
            access_token=token,
            user=user,
        )

    def __get_user_token(self, user_id, user_role) -> str:
        payload = {
            'user_id': str(user_id),
            'role': user_role,
        }
        return jwt_handler.encode(payload)
