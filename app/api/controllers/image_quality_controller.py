from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.image_quality_service import ImageQualityService

router = APIRouter(
    prefix="/images",
    tags=["Image Quality"]
)

# temporalmente dejamos thresholds aqui
threshold_metrics = {
    "brightness": {
        "min": 30,
        "max": 220
    },
    "contrast": {
        "min": 20
    },
    "entropy": {
        "min": 4
    },
    "dynamic_range": {
        "min": 50
    },
    "blur_score": {
        "min": 100
    },
    "underexposed_ratio": {
        "max": 0.15
    },
    "overexposed_ratio": {
        "max": 0.10
    },
    "noise_estimate": {
        "max": 15
    }
}

service = ImageQualityService(threshold_metrics)

@router.post("/quality")
async def analyze_image_quality(file: UploadFile = File(...)):
    """
    Analiza la calidad técnica de una radiografía.
    """

    try:
        image_bytes = await file.read()
        result = service.analyze(image_bytes)
        return result

    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))