from fastapi import FastAPI
from database import engine
from models.db_models import Base
from routes import live, forecast, history
from services.scheduler import start_scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ocean Forecasting & Risk API")

app.include_router(live.router)
app.include_router(forecast.router)
app.include_router(history.router)


@app.on_event("startup")
def start_background_tasks():
    start_scheduler()