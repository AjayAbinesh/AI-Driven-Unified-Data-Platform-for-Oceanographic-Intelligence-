from fastapi import APIRouter
from database import SessionLocal
from models.db_models import OceanData

router = APIRouter()

@router.get("/history")
def get_history():

    db = SessionLocal()

    data = db.query(OceanData).order_by(OceanData.id.desc()).limit(20).all()

    result = []

    for row in data:
        result.append({
            "timestamp": row.timestamp,
            "wave_height": row.wave_height,
            "prediction": row.predicted_wave
        })

    db.close()

    return result