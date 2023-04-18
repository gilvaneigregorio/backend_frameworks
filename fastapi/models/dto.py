import typing
from pydantic import BaseModel
from pydantic import BaseModel, validator


class Product(BaseModel):
    id: int
    name: str
    computed_field: typing.Optional[str]

    @validator('computed_field', pre=True, always=True)
    def make_computed_field(cls, v: str, values: dict):
        return f'{values["name"]}_{values["id"]}'

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str
