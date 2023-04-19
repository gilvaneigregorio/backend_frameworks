import uvicorn

from fastapi import FastAPI
from routers import categories, products
from utils.databases import Base, engine

app = FastAPI()

app.include_router(categories.router)
app.include_router(products.router)


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
