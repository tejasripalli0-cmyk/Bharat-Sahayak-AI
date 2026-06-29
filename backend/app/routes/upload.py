"""
Bharat Sahayak AI
Upload Router
"""

from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/document")
async def upload_document(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Document uploaded successfully"
    }


@router.post("/audio")
async def upload_audio(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Audio uploaded successfully"
    }
