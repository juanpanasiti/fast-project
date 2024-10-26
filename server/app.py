# import logging

from fastapi import FastAPI

from .api import api_router


# logger = logging.getLogger(__name__)
fast_projects = FastAPI()

# Incluimos el router principal a la instancia de FastAPI
fast_projects.include_router(api_router)


# @fast_projects.on_event('startup')
# async def startup_event():
#     logger.debug('API Iniciada')


# @fast_projects.on_event('shutdown')
# def shutdown_event():
#     logger.debug('API Finalizada')
