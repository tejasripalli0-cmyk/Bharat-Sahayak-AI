"""
Bharat Sahayak AI
Translation Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/translation",
    tags=["Translation"],
)

@router.post("/translate")
def translate():
    return {"message":"Translate endpoint ready"}

@router.get("/languages")
def languages():
    return {"message":"Supported languages endpoint ready"}

@router.get("/history/{user_id}")
def history(user_id:int):
    return {"message":"Translation history endpoint ready","user_id":user_id}
