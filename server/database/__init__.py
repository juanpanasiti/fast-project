from server.configs import app_settings
from .database_connection import DatabaseConnection
from .models import BaseModel


db_connection = DatabaseConnection(app_settings.DB_CONN)
def create_tables():
    BaseModel.metadata.create_all(bind=db_connection.engine)
