import pytest
from httpx import AsyncClient

from src.app.main import app

base_url = "http://127.0.0.1:8000"


@pytest.mark.asyncio
async def test_root():
    """
    Summary:
    Test the health check endpoint of the API.

    Args:
    None

    Returns:
    None

    Raises:
    None
    """
    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.get("/api/v1/health-checker")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_main_redirect():
    """
    Summary:
    Test the main redirect functionality of the API.

    Args:
    None

    Returns:
    None

    Raises:
    None
    """

    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.get("/api/v1/")
    assert response.status_code == 307
    assert response.headers["location"] == "/docs/"
