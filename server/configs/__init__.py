from .settings import Settings
from .logging import config_logger

app_settings = Settings()
config_logger(app_settings.DEBUG)
