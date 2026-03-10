from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
import logging

from fastapi import FastAPI
from src.api.routes import todo, reminder, calendar_event, call, memory
from src.models.database import create_tables

logging.basicConfig(
    level=getattr(logging, "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("Starting application, initializing database...")
    create_tables()
    logger.info("Application startup complete!")
    yield
    logger.info("Application shutdown")

app = FastAPI(title="Personal Assistant Voice Agent", lifespan=lifespan)

# Include routers
app.include_router(todo.router)
app.include_router(reminder.router)
app.include_router(calendar_event.router)
app.include_router(call.router)
app.include_router(memory.router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)