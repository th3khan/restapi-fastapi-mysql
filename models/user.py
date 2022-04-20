from sqlalchemy import Table, Column
from sqlalchemy.types import BigInteger, String
from config.db import meta, engine

users = Table(
    "users",
    meta,
    Column("id", BigInteger, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), nullable=False),
    Column("password", String(255), nullable=False),
)

meta.create_all(engine)