from fastapi import APIRouter, UploadFile, File, Form
import shutil

from app.textract_service import extract_text_from_file

router = APIRouter()


@router.post("/verify-label")
async def verify_label(
    file: UploadFile = File(...),
    brand_name: str = Form(...),
    class_type: str = Form(...),
    alcohol_content: str = Form(...),
    net_contents: str = Form(...),
    government_warning: str = Form(...)
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ocr_text = extract_text_from_file(file_path)

    text = ocr_text.upper()

    brand_match = brand_name.upper() in text
    class_type_match = class_type.upper() in text
    abv_match = alcohol_content.upper() in text
    net_contents_match = net_contents.upper() in text
    government_warning_match = (
        government_warning.upper() in text
    )

    if (
        brand_match
        and class_type_match
        and abv_match
        and net_contents_match
        and government_warning_match
    ):
        status = "PASS"
    else:
        status = "REVIEW"

    return {
        "filename": file.filename,
        "ocr_text": ocr_text,
        "brand_match": brand_match,
        "class_type_match": class_type_match,
        "abv_match": abv_match,
        "net_contents_match": net_contents_match,
        "government_warning_match": government_warning_match,
        "status": status
    }
