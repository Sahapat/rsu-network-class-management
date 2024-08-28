from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import app_settings
from .dependency import inject_dependencies
from .controllers import assignment_upload_api

import logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


def init_app():
    app = FastAPI(
        title="RSU Game Network Class",
        description="Utility API for RSU Game Network Class",
        version="1"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def startup():
        logger.debug('Inject dependencies')
        inject_dependencies()
        logger.debug('Start dependencies')

    @app.on_event("shutdown")
    async def shutdown():
        pass

    app.include_router(assignment_upload_api, prefix='/api/v1',)
    return app


app = init_app()
