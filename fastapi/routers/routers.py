from typing import List

import fastapi
from models.dto import ProductCreate, Product
from models.dao import products
from utils.databases import database


router = fastapi.APIRouter()


@router.get("/product/{product_id}", response_model=Product)
async def get_product_by_id(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@ router.get("/products/", response_model=List[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@ router.post("/products/")
async def create_product(product_create: ProductCreate, status_code=201):
    query = products.insert().values(name=product_create.name)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, **product_create.dict()}


@ router.put("/products/{product_id}")
async def update_product(product_id: int, name: str):
    query = products.update().where(products.c.id == product_id).values(name=name)
    await database.execute(query)
    return {"id": product_id, "name": name}


@ router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {"message": f"Product with id {product_id} deleted successfully!"}
