import sqlalchemy
from sqlalchemy import Column, Integer, String

from utils.databases import metadata

products = sqlalchemy.Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, unique=True, index=True),
)
