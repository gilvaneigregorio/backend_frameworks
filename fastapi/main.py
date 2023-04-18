from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

products = []


class Product(BaseModel):
    id: int
    name: str


class ProductCreate(BaseModel):
    name: str


@app.get("/product/{product_id}")
async def get_product_by_id(product_id: int):
    return products[product_id]


@app.get("/products/")
async def get_products():
    return products


@app.post("/products/")
async def create_product(product_create: ProductCreate, status_code=201):
    id = len(products)
    product = Product(id=id, name=product_create.name)
    products.append(product)
    return product


@app.put("/products/{product_id}")
async def update_product(product_id: int, name: str):
    product = products[product_id]
    product.name = name
    return product


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    products.pop(product_id)
    return products
