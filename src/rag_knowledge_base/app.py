from __future__ import annotations

import logging
from fastapi import FastAPI
from .api.routers import router
from .core.config import AppSettings

logging.basicConfig(level=logging.INFO)
app = FastAPI(title=AppSettings().app_name)
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {"message": f"Welcome to {AppSettings().app_name}"}
