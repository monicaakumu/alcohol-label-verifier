from fastapi import FastAPI

from app.models import LabelRequest
from app.upload import router as upload_router
from app.verify_label import router as verify_label_router

app = FastAPI(title="Alcohol Label Verification API")

app.include_router(upload_router)
app.include_router(verify_label_router)


@app.get("/")
def root():
    return {
        "message": "Alcohol Label Verification API Running"
    }


@app.post("/verify")
def verify_label(request: LabelRequest):
    text = request.ocr_text.upper()

    brand_match = request.brand_name.upper() in text
    class_type_match = request.class_type.upper() in text
    abv_match = request.alcohol_content.upper() in text
    net_contents_match = request.net_contents.upper() in text
    government_warning_match = (
        request.government_warning.upper() in text
    )

    status = "PASS" if (
        brand_match
        and class_type_match
        and abv_match
        and net_contents_match
        and government_warning_match
    ) else "REVIEW"

    return {
        "brand_match": brand_match,
        "class_type_match": class_type_match,
        "abv_match": abv_match,
        "net_contents_match": net_contents_match,
        "government_warning_match": government_warning_match,
        "status": status
    }
