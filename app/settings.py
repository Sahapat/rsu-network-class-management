from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

import logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict()
    DB_USER: str = ''
    DB_PASSWORD: str = ''
    DB_NAME: str = ''
    DB_HOST: str = ''
    DB_PORT: str = ''
    API_KEY: str = ''
    ALLOW_ORIGINS: List[str] = ['*']

    @property
    def DB_CONFIG(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


app_settings = AppSettings()
logger.info("=== Application Settings ===")
logger.info(app_settings.model_dump())
