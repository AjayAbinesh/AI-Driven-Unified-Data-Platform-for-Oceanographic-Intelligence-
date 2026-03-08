import pandas as pd
from config import LIVE_URL
from database import SessionLocal
from models.db_models import OceanData

def fetch_live_data():

    df = pd.read_csv(LIVE_URL, delim_whitespace=True, comment="#")
    latest = df.iloc[-1]

    wave = latest["WVHT"]
    wind = latest["WSPD"]
    pressure = latest["PRES"]

    db = SessionLocal()

    record = OceanData(
        wave_height=wave,
        wind_speed=wind,
        pressure=pressure
    )

    db.add(record)
    db.commit()
    db.close()

    return {
        "wave_height": wave,
        "wind_speed": wind,
        "pressure": pressure
    }