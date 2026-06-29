"""
Bharat Sahayak AI
API Key Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"],
)


@router.get("/")
def list_api_keys():
    return {
        "message": "API keys endpoint ready"
    }


@router.post("/")
def create_api_key():
    return {
        "message": "API key created"
    }


@router.put("/{key_id}")
def update_api_key(key_id: int):
    return {
        "message": "API key updated",
        "key_id": key_id,
    }


@router.delete("/{key_id}")
def delete_api_key(key_id: int):
    return {
        "message": "API key deleted",
        "key_id": key_id,
    }