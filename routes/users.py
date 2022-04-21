from fastapi import APIRouter, status
from typing import List
from config.db import conn
from models.user import users
from schemas.user import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user_routes = APIRouter()

@user_routes.get("/users", response_model=List[User], status_code=status.HTTP_200_OK)
def get_users():
    return conn.execute(users.select()).fetchall()

@user_routes.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email
    }
    new_user["password"] = f.encrypt(user.password.encode("utf-8")).decode("utf-8")
    print(new_user)
    result = conn.execute(users.insert(), new_user)
    print(result)
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user_routes.get("/users/{id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user_routes.delete("/users/{id}")
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return {"message": "User deleted"}

@user_routes.put("/users/{id}", response_model=User, status_code=status.HTTP_200_OK)
def update_user(id: int, user: User):
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": f.encrypt(user.password.encode("utf-8")).decode("utf-8")
    }
    conn.execute(users.update().where(users.c.id == id), new_user)
    return {
        "message": "User updated",
        "data": conn.execute(users.select().where(users.c.id == id)).first()
    }
    