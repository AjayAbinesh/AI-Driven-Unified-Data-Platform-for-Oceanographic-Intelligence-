from sqlalchemy import Column, Integer, Float, DateTime
from database import Base
import datetime

class OceanData(Base):
    __tablename__ = "ocean_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    wave_height = Column(Float)
    wind_speed = Column(Float)
    pressure = Column(Float)
    predicted_wave = Column(Float)