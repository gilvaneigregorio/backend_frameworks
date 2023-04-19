from typing import List

import fastapi
from models.dto import CategoryCreate, Category as CategoryDTO
from models.dao import Category
from utils.databases import async_session
from sqlalchemy import update, select, delete

router = fastapi.APIRouter()


@router.get("/categories/{category_id}", response_model=CategoryDTO)
async def get_category_by_id(category_id: int):
    async with async_session() as db:
        async with db.begin():
            query = select(Category).where(Category.id == category_id)
            result = await db.execute(query)
            return result.scalars().first()


@ router.get("/categories/", response_model=List[CategoryDTO])
async def get_categories():
    async with async_session() as db:
        async with db.begin():
            query = select(Category)
            result = await db.execute(query)
            return result.scalars().all()


@ router.post("/categories/", status_code=201)
async def create_category(category_create: CategoryCreate):
    async with async_session() as db:
        async with db.begin():
            category = Category(name=category_create.name,
                                description=category_create.description)
            db.add(category)
            await db.commit()
            return category


@ router.put("/categories/{category_id}")
async def update_category(category_id: int, name: str, description: str):
    async with async_session() as db:
        async with db.begin():
            query = update(Category).where(Category.id == category_id).values(
                name=name, description=description)
            await db.execute(query)
            await db.commit()
            return {"message": f"Category with id {category_id} updated successfully!"}


@ router.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    async with async_session() as db:
        async with db.begin():
            query = delete(Category).where(Category.id == category_id)
            await db.execute(query)
            await db.commit()
            return {"message": f"Category with id {category_id} deleted successfully!"}
