from uuid import UUID
from typing import Dict, List
from app.base.singleton import Singleton

import logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Registry(metaclass=Singleton):
    def __init__(self):
        pass
