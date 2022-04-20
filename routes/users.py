from fastapi import APIRouter
from config.db import conn
from models.user import users

user_routes = APIRouter()

@user_routes.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()