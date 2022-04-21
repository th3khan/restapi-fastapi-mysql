from typing import Any


def create_response(message: str, data: Any = None):
    return {
        "message": message,
        "data": data
    }