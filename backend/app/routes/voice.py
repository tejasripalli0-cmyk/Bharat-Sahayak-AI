"""
Bharat Sahayak AI
Voice Router
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/voice",
    tags=["Voice"],
)

@router.post("/speech-to-text")
def speech_to_text():
    return {"message":"Speech-to-Text endpoint ready"}

@router.post("/text-to-speech")
def text_to_speech():
    return {"message":"Text-to-Speech endpoint ready"}

@router.get("/history/{user_id}")
def history(user_id:int):
    return {"message":"Voice history endpoint ready","user_id":user_id}
