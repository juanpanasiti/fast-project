from .settings import Settings
from .logging import config_logger
from .api_doc import api_description

app_settings = Settings()
config_logger(app_settings.DEBUG)
