from typing import Annotated, List

from fastapi import APIRouter, Path, Query, Depends

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.schemas.auth_schemas import DecodedJwt
from server.controller import ProjectsController
from server.exceptions import InternalServerError, NotFound
from server.dependencies import has_permission
from server.enums import ALL_ROLES

router = APIRouter(prefix='/projects')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = ProjectsController()


@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Proyecto creado'},
    },
    description='Crea un proyecto nuevo con los campos pasados por Body Param. Falla si faltan alguno de los campos obligatorios.'
)  # POST /projects
async def create(
    new_project: NewProjectRequest,
    token: DecodedJwt = Depends(has_permission(ALL_ROLES)),
) -> ProjectResponse:
    return controller.create(new_project, token.user_id)


@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Listado de proyectos'},
    },
    description='Retorna una lista paginada con los proyectos del usuario. Si no hay proyectos para mostrar, retorna lista vacía.'
)  # GET /projects
async def get_list(
    limit: Annotated[int, Query(ge=1, le=1000)] = 10,
    offset: Annotated[int, Query(ge=0)] = 0,
    token: DecodedJwt = Depends(has_permission(ALL_ROLES)),
) -> List[ProjectResponse]:
    return controller.get_list(limit, offset, token.user_id)


@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Retorna un proyecto por ID. Falla si el ID no existe.'
)  # GET /projects/{id}
async def get_by_id(
    id: Annotated[int, Path(ge=1)],
    token: DecodedJwt = Depends(has_permission(ALL_ROLES)),
) -> ProjectResponse:
    return controller.get_by_id(id, token)


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Actualiza un proyecto con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /projects/{id}
async def update(
    id: Annotated[int, Path(ge=1)],
    project: ProjectRequest,
    token: DecodedJwt = Depends(has_permission(ALL_ROLES)),
) -> ProjectResponse:
    return controller.update(id, project, token)


@router.delete(
    '/{id}',
    status_code=204,
    responses={
        204: {'description': 'Proyecto eliminado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Elimina un proyecto con id pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /projects/{id}
async def delete(
    id: Annotated[int, Path(ge=1)],
    token: DecodedJwt = Depends(has_permission(ALL_ROLES)),
) -> None:
    controller.delete(id, token)
