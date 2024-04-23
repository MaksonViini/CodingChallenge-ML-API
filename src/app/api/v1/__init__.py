from fastapi import APIRouter

from .health_check import router as health_check_router
from .ml_model import router as ml_model_router

router = APIRouter(prefix="/v1")
router.include_router(health_check_router)
router.include_router(ml_model_router)
