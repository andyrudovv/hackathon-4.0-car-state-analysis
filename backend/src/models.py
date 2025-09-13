from pydantic import BaseModel
from typing import List, Optional

class PhotoUpload(BaseModel):
    filename: str
    content_type: str
    data: bytes

class PhotoAnalyticsResult(BaseModel):
    filename: str
    analysis: dict

class PhotoAnalyticsRequest(BaseModel):
    photos: List[PhotoUpload]

class PhotoAnalyticsResponse(BaseModel):
    results: List[PhotoAnalyticsResult]