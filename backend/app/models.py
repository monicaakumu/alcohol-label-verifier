from pydantic import BaseModel


class LabelRequest(BaseModel):
    brand_name: str
    alcohol_content: str
    net_contents: str
