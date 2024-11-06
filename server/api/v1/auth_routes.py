from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


from server.schemas.auth_schemas import RegisterUser, LoginUser, TokenResponse
from server.controller import AuthController
from server.exceptions import InternalServerError, BadRequest


router = APIRouter(prefix='/auth')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = AuthController()

@router.post(
    '/register',
    status_code=201,
    responses={
        201: {'description': 'Usuario registrado'},
        400: {'description': BadRequest.description},
    }
)
async def register_user(new_user: RegisterUser) -> TokenResponse:
    return controller.register(new_user)

@router.post(
    '/login',
    responses={
        200: {'description': 'Usuario logeado'},
        400: {'description': BadRequest.description},
    }
)
async def login_user(credentials: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    return controller.login(credentials)

