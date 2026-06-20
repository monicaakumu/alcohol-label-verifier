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

    return {
        "brand_name": request.brand_name,
        "alcohol_content": request.alcohol_content,
        "net_contents": request.net_contents,
        "status": "Verification endpoint working"
        }
