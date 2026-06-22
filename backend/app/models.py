from pydantic import BaseModel


class LabelRequest(BaseModel):
    brand_name: str
    class_type: str
    alcohol_content: str
    net_contents: str
    government_warning: str
    ocr_text: str


class VerifyLabelRequest(BaseModel):
    brand_name: str
    class_type: str
    alcohol_content: str
    net_contents: str
    government_warning: str
