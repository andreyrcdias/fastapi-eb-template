import pytest
from fastapi.testclient import TestClient

from src.server import create_app


@pytest.fixture
def test_client():
    app = create_app()
    yield TestClient(app)
