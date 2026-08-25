from typing import Any


def success(data: Any) -> dict[str, Any]:
    return {
        "success": True,
        "data": data,
    }


def error(message: str) -> dict[str, Any]:
    return {
        "success": False,
        "error": message,
    }
