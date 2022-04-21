from fastapi import APIRouter, status
from typing import List
from config.db import conn
from models.user import users
from schemas.response import ResponseBase
from schemas.user import User
from helpers.response import create_response

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user_routes = APIRouter()

@user_routes.get("/users", response_model=List[User], status_code=status.HTTP_200_OK, tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user_routes.post("/users", response_model=ResponseBase[User], status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email
    }
    new_user["password"] = f.encrypt(user.password.encode("utf-8")).decode("utf-8")
    result = conn.execute(users.insert(), new_user)
    return create_response(
        message="User created successfully",
        data=conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    )

@user_routes.get("/users/{id}", response_model=User, status_code=status.HTTP_200_OK, tags=["users"])
def get_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user_routes.delete("/users/{id}", tags=["users"], response_model=ResponseBase, status_code=status.HTTP_200_OK)
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return create_response(message="User deleted successfully", data=None)

@user_routes.put("/users/{id}", response_model=ResponseBase[User], status_code=status.HTTP_200_OK, tags=["users"])
def update_user(id: int, user: User):
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": f.encrypt(user.password.encode("utf-8")).decode("utf-8")
    }
    conn.execute(users.update().where(users.c.id == id), new_user)
    return create_response(
        message="User updated successfully",
        data=conn.execute(users.select().where(users.c.id == id)).first()
    )    