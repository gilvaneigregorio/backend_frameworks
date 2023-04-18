from fastapi import FastAPI

from routers.routers import router
from utils.databases import metadata, engine

app = FastAPI()

app.include_router(router, prefix="/v1")

metadata.create_all(engine)
