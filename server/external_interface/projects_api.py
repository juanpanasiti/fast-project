import logging

import requests

from server.configs import app_settings


logger = logging.getLogger(__name__)


class ProjectsApi:
    def __init__(self):
        self.client = requests.Session()
        self.base_url = app_settings.PROJECTS_API

    def get_list(self, limit: int, offset: int):
        # url = self.base_url + f'/projects?limit={limit}&offset={offset}'
        url = self.base_url + '/projects'  # recomendada
        params = {
            'limit': limit,
            'offset': offset,
        }
        response = self.client.get(url, params=params)
        logger.info(f'[GET] {response.url}: {response.status_code}')

        return response.json()
