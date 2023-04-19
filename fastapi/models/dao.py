import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey

from utils.databases import metadata, Base


class Category(Base):
    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    products = sqlalchemy.orm.relationship(
        "Product", back_populates="category", lazy="subquery")


class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category_id = Column(ForeignKey("Category.id"), nullable=False)
    category = sqlalchemy.orm.relationship(
        "Category", back_populates="products", lazy="joined")
