import fastapi
from fastapi import Request, HTTPException
from ...schemas.ml_model import Input, Output
from ...resources.load import load_model, load_scaler
import pandas as pd
from ...core.logger import logging
from ...core.config import settings

router = fastapi.APIRouter(tags=["ML Model Predict"])

logger = logging.getLogger(__name__)
DEFAULT_LIMIT = settings.DEFAULT_RATE_LIMIT_LIMIT
DEFAULT_PERIOD = settings.DEFAULT_RATE_LIMIT_PERIOD

# Load the ML model and scaler once when the application starts
model = load_model()
scaler = load_scaler()


@router.post("/predict", response_model=Output)
async def predict(
    request: Request,
    input_data: Input,
):
    """
    Predicts the output using the pre-trained machine learning model.

    Args:
        request (Request): The incoming HTTP request.
        input_data (Input): The input data for prediction.

    Returns:
        dict: A dictionary containing the predicted output.

    Raises:
        HTTPException: If prediction fails, returns a 500 status code with an error message.
    """
    try:
        data = pd.DataFrame([input_data.dict()])

        data_std = scaler.transform(data)

        pred = model.predict(data_std)

        logger.info(f"Prediction succeeded: Prediction is {int(pred[0])}")

        return {"Predicted": int(pred[0])}

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed") from e
