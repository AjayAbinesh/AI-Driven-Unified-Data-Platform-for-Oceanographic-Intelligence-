from fastapi import APIRouter
from services.risk_engine import calculate_risk
from services.live_fetch import fetch_live_data

router = APIRouter()

@router.get("/risk")
def risk():
    live_data = fetch_live_data()
    wave = live_data["wave_height"]
    risk_level = calculate_risk(wave)

    return {
        "current_wave": wave,
        "risk_level": risk_level
    }