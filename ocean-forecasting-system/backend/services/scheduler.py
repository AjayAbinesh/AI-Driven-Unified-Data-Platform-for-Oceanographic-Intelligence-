from apscheduler.schedulers.background import BackgroundScheduler
from services.live_fetch import fetch_live_data
from services.forecasting import predict_wave

def scheduled_job():
    try:
        live_data = fetch_live_data()
        prediction = predict_wave(live_data)

        print("Live data fetched")
        print("Prediction:", prediction)

    except Exception as e:
        print("Scheduler error:", e)


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Run every 10 minutes
    scheduler.add_job(scheduled_job, "interval", minutes=10)

    scheduler.start()