from fastapi import APIRouter, UploadFile, File
import shutil
from config import UPLOAD_PATH

router = APIRouter()

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    with open(UPLOAD_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "File uploaded"}
