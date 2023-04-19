import typing

from pydantic import BaseModel, validator


class CategoryBase(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Product(ProductBase):
    category: typing.Optional["CategoryBase"]
    computed_field: typing.Optional[str]

    @validator("computed_field", pre=True, always=True)
    def make_computed_field(cls, v: str, values: dict):
        return f'{values["name"]}_{values["id"]}'

    class Config:
        orm_mode = True


class Category(CategoryBase):
    products: typing.Optional[typing.List[ProductBase]]


class ProductCreate(BaseModel):
    name: str
    category_id: int


class CategoryCreate(BaseModel):
    name: str
    description: str
