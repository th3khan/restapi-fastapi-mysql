from fastapi import FastAPI

from routes.users import user_routes

app = FastAPI(
    title="My FastAPI App",
    description="This is my FastAPI App",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations about users"
        }
    ]
)
app.include_router(user_routes)