import pytest
from httpx import AsyncClient

from src.app.main import app
import json

from tests.utils.predict import create_random_data_to_predict

base_url = "http://127.0.0.1:8000"


@pytest.mark.asyncio
async def test_predict():
    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.post(
            "/api/v1/predict", json=create_random_data_to_predict()
        )
    assert response.status_code == 200
