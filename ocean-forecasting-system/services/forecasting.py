import joblib
import pandas as pd
from config import MODEL_PATH
from database import SessionLocal
from models.db_models import OceanData

model = joblib.load(MODEL_PATH)

def predict_wave(live_data):

    db = SessionLocal()

    last_record = db.query(OceanData).order_by(OceanData.id.desc()).first()

    last_wave = last_record.wave_height if last_record else 2.0

    input_df = pd.DataFrame([{
        "WSPD": live_data["wind_speed"],
        "PRES": live_data["pressure"],
        "lag_1": last_wave
    }])

    prediction = model.predict(input_df)[0]

    last_record.predicted_wave = float(prediction)

    db.commit()
    db.close()

    return prediction