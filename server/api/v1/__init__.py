from fastapi import APIRouter

from .project_routes import router as project_router
from .user_routes import router as user_router
from .auth_routes import router as auth_router

# Router V1
router_v1 = APIRouter(prefix='/v1')

# Agregamos al router v1 las rutas definidas
router_v1.include_router(auth_router, tags=['Auth'])
router_v1.include_router(project_router, tags=['Projects'])
router_v1.include_router(user_router, tags=['Users'])
