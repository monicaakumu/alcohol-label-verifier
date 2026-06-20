from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/upload-label")
async def upload_label(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "uploaded successfully"
    }
