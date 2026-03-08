from fastapi import APIRouter
from services.live_fetch import fetch_live_data

router = APIRouter()

@router.get("/live")
def get_live():
    return fetch_live_data()