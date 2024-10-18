from fastapi import APIRouter

from .v1 import router_v1


# Router API
api_router = APIRouter(prefix='/api')
api_router.include_router(router_v1)
