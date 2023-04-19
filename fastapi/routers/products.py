from typing import List

import fastapi
from models.dto import ProductCreate, Product as ProductDTO
from models.dao import Product
from utils.databases import async_session
from sqlalchemy import update, select, delete

router = fastapi.APIRouter()


@router.get("/products/{product_id}", response_model=ProductDTO)
async def get_product_by_id(product_id: int):
    async with async_session() as db:
        async with db.begin():
            query = select(Product).where(Product.id == product_id)
            result = await db.execute(query)
            return result.scalars().first()


@ router.get("/products/", response_model=List[ProductDTO])
async def get_products():
    async with async_session() as db:
        async with db.begin():
            query = select(Product)
            result = await db.execute(query)
            return result.scalars().all()


@ router.post("/products/", status_code=201)
async def create_product(product_create: ProductCreate):
    async with async_session() as db:
        async with db.begin():
            product = Product(name=product_create.name,
                              category_id=product_create.category_id)
            db.add(product)
            await db.commit()
            return product


@ router.put("/products/{product_id}")
async def update_product(product_id: int, name: str, description: str, category_id: int):
    async with async_session() as db:
        async with db.begin():
            query = update(Product).where(Product.id == product_id).values(
                name=name, description=description, category_id=category_id)
            await db.execute(query)
            await db.commit()
            return {"message": f"Product with id {product_id} updated successfully!"}


@ router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    async with async_session() as db:
        async with db.begin():
            query = delete(Product).where(Product.id == product_id)
            await db.execute(query)
            await db.commit()
            return {"message": f"Product with id {product_id} deleted successfully!"}
