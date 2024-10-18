from fastapi import APIRouter

router = APIRouter(prefix='/projects')


@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Listado de proyectos'},
    },
    description='Retorna una lista paginada con los proyectos del usuario. Si no hay proyectos para mostrar, retorna lista vacía.'
)  # GET /projects
async def get_list() -> list:
    return []


@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Proyecto creado'},
    },
    description='Crea un proyecto nuevo con los campos pasados por Body Param. Falla si faltan alguno de los campos obligatorios.'
)  # POST /projects
async def create() -> dict:
    return {}


@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto encontrado'},
        422: {'description': 'ID no es un entero válido'},
    },
    description='Retorna un proyecto por ID. Falla si el ID no existe.'
)  # GET /projects/{id}
async def get_by_id(id: int) -> dict:
    return {'id': id}


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto actualizado'},
        422: {'description': 'ID no es un entero válido'},
    },
    description='Actualiza un proyecto con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /projects/{id}
async def update(id: int) -> dict:
    return {'id': id}


@router.delete(
    '/{id}',
    status_code=204,
    responses={
        204: {'description': 'Proyecto eliminado'},
        422: {'description': 'ID no es un entero válido'},
    },
    description='Elimina un proyecto con id pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /projects/{id}
async def delete(id: int) -> None:
    return None
