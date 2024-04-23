import pytest
from httpx import AsyncClient

from src.app.main import app

from tests.utils.predict import create_random_data_to_predict

base_url = "http://127.0.0.1:8000"

input_data = {
  "sample_code_number": 999999,
  "clump_thickness": 5,
  "uniformity_of_cell_size": 10,
  "uniformity_of_cell_shape": 10,
  "marginal_adhesion": 3,
  "single_epithelial_cell_size": 7,
  "bare_nuclei": 3,
  "bland_chromatin": 8,
  "normal_nucleoli": 10,
  "mitoses": 2
}

@pytest.mark.asyncio
async def test_predict():
    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.post(
            "/api/v1/predict", data=input_data
        )
    assert response.status_code == 200
