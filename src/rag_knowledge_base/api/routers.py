from __future__ import annotations

from fastapi import APIRouter
from . import schemas
from ..core.config import AppSettings, HealthResponse
from ..services.rag import RagService

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    settings = AppSettings()
    return HealthResponse(status="ok", name=settings.app_name)


@router.post("/run", response_model=schemas.RunResponse)
async def run_endpoint(body: schemas.RunRequest) -> schemas.RunResponse:
    service = RagService(model_name=body.model_name)
    result = await service.run(body.payload)
    return schemas.RunResponse(**result)
