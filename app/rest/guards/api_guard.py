from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader
from app.settings import app_settings

import logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def api_key_guard(x_api_key: str = Depends(APIKeyHeader(name="x-api-key"))):
    if x_api_key != app_settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API KEY")
