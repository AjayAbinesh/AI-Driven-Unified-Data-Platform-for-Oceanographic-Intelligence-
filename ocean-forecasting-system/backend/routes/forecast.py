from fastapi import APIRouter
from services.live_fetch import fetch_live_data
from services.forecasting import predict_wave

router = APIRouter()

last_wave = 2.0  # simple placeholder

@router.get("/forecast")
def forecast():
    global last_wave
    live_data = fetch_live_data()
    prediction = predict_wave(live_data, last_wave)
    last_wave = prediction

    return {
        "predicted_wave_height": prediction
    }