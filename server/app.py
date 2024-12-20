# import logging

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from .api import api_router
from .database import db_connection
from .configs import api_description
from .middlewares import RequestLoggingMiddleware, JwtMiddleware


api_middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        expose_headers=['renewed-token']
    ),
    Middleware(JwtMiddleware),
    Middleware(RequestLoggingMiddleware),
]


# logger = logging.getLogger(__name__)
fast_projects = FastAPI(
    middleware=api_middlewares,
    **api_description
    )

# Incluimos el router principal a la instancia de FastAPI
fast_projects.include_router(api_router)


@fast_projects.on_event('startup')
async def startup_event():
    # if db_connection.connect():
    #     create_tables()
    db_connection.connect()


@fast_projects.on_event('shutdown')
def shutdown_event():
    db_connection.disconnect()
