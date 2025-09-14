from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from src.services.analytics import analyze_photo
from PIL import Image
import io

router = APIRouter()

@router.post("/upload/")
async def upload_photo(file: UploadFile = File(...)):
    # Read the image file
    contents = await file.read()
    # print(contents)
    image = Image.open(io.BytesIO(contents))
    print(image)

    # Process the uploaded photo using the custom AI model
    analytics_result = analyze_photo(image)
    
    return {"filename": file.filename, "analytics": analytics_result}

@router.get("/analytics/{photo_id}")
async def get_analytics(photo_id: str):
    # Here you would retrieve the analytics result for the given photo_id
    # This is a placeholder implementation
    analytics_result = {"photo_id": photo_id, "result": "Sample analytics result"}
    
    return analytics_result