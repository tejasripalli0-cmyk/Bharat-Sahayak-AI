"""
Bharat Sahayak AI
System Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get("/health")
def health():
    return {"message": "System health endpoint ready"}


@router.get("/info")
def info():
    return {"message": "System info endpoint ready"}


@router.get("/version")
def version():
    return {"version": "1.0.0"}


@router.get("/status")
def status():
    return {"status": "running"}
