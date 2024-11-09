from typing import Annotated, List

from fastapi import APIRouter, Path, Query, Depends

from server.schemas.user_schemas import NewUserRequest, UserResponse, UserRequest
from server.schemas.auth_schemas import DecodedJwt
from server.controller import UsersController
from server.exceptions import InternalServerError, NotFound
from server.dependencies import has_permission
from server.enums import ADMIN_ROLES

router = APIRouter(prefix='/users')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = UsersController()


@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Usuario creado'},
    },
    description='Crea un usuario nuevo con los campos pasados por Body Param. Falla si faltan alguno de los campos obligatorios.'
)  # POST /users
async def create(
    new_user: NewUserRequest,
    _: DecodedJwt = Depends(has_permission(ADMIN_ROLES)),
) -> UserResponse:
    return controller.create(new_user)


@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Listado de usuarios'},
    },
    description='Retorna una lista paginada con los usuarios del usuario. Si no hay usuarios para mostrar, retorna lista vacía.'
)  # GET /users
async def get_list(
    limit: Annotated[int, Query(ge=1, le=1000)] = 10,
    offset: Annotated[int, Query(ge=0)] = 0,
    _: DecodedJwt = Depends(has_permission(ADMIN_ROLES))
) -> List[UserResponse]:
    return controller.get_list(limit, offset)


@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Usuario encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Retorna un usuario por ID. Falla si el ID no existe.'
)  # GET /users/{id}
async def get_by_id(
    id: Annotated[int, Path(ge=1)],
    _: DecodedJwt = Depends(has_permission(ADMIN_ROLES)),
) -> UserResponse:
    return controller.get_by_id(id)


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Usuario actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Actualiza un usuario con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /users/{id}
async def update(
    id: Annotated[int, Path(ge=1)],
    user: UserRequest,
    _: DecodedJwt = Depends(has_permission(ADMIN_ROLES)),
) -> UserResponse:
    return controller.update(id, user)


@router.delete(
    '/{id}',
    status_code=204,
    responses={
        204: {'description': 'Usuario eliminado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Elimina un usuario con id pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /users/{id}
async def delete(
    id: Annotated[int, Path(ge=1)],
    _: DecodedJwt = Depends(has_permission(ADMIN_ROLES)),
) -> None:
    controller.delete(id)
