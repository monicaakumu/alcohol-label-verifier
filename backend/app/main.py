from fastapi import FastAPI

from app.models import LabelRequest
from app.upload import router as upload_router

app = FastAPI(
    title="Alcohol Label Verification API"
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "Alcohol Label Verification API Running"
    }


@app.post("/verify")
def verify_label(request: LabelRequest):

    text = request.ocr_text.upper()

    brand_match = request.brand_name.upper() in text
    abv_match = request.alcohol_content.upper() in text
    net_contents_match = request.net_contents.upper() in text

    if brand_match and abv_match and net_contents_match:
        status = "PASS"
    else:
        status = "REVIEW"

    return {
        "brand_match": brand_match,
        "abv_match": abv_match,
        "net_contents_match": net_contents_match,
        "status": status
    }
