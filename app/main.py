from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()

    print(f"{settings.app_name} started")

    yield

    print("Application stopped")


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "message": "Finance Quiz API",
        "docs": "/docs",
    }


app.include_router(
    health_router,
    prefix="/api/v1",
)