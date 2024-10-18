from fastapi import FastAPI

from .api import api_router

fast_projects = FastAPI()

# Incluimos el router principal a la instancia de FastAPI
fast_projects.include_router(api_router)
