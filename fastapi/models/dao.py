import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey

from utils.databases import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    products = sqlalchemy.orm.relationship(
        "products", back_populates="category", lazy="subquery")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category_id = Column(ForeignKey("categories.id"), nullable=False)
    category = sqlalchemy.orm.relationship(
        "categories", back_populates="products", lazy="joined")
