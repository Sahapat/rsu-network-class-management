# test_main.py
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.rest.main import app
from app.registry import Registry
from app.settings import app_settings


class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestExample(app)

if __name__ == '__main__':
    unittest.main()
