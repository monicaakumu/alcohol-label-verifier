from fastapi import APIRouter, UploadFile, File
import shutil

from app.textract_service import extract_text_from_file

router = APIRouter()


@router.post("/upload-label")
async def upload_label(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_to": file_path,
        "status": "uploaded successfully"
    }


@router.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_file(file_path)

    return {
        "filename": file.filename,
        "text": extracted_text
    }
