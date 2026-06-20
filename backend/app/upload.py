from fastapi import APIRouter, UploadFile, File
import shutil

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
