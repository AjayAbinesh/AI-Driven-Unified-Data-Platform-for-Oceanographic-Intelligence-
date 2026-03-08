🌊 AI-Driven Oceanographic Forecasting & Risk Monitoring Platform

An intelligent platform that monitors ocean conditions in near real-time, predicts wave heights using machine learning, and assesses coastal risk levels through a clean interactive dashboard.

The system integrates historical buoy datasets and live ocean sensor data to provide predictive insights for safer maritime and coastal monitoring.

📌 Features

🌊 Real-time ocean data monitoring

📈 Machine learning based wave height forecasting

⚠️ Coastal risk classification (Low / Medium / High)

🧠 Historical data training for predictive modeling

🔄 Automated live data updates using scheduler

📊 Interactive React dashboard visualization

💾 Database storage for historical and live data

🏗 System Architecture
Ocean Buoy Sensors
        ↓
Live Ocean API (NOAA Buoy Data)
        ↓
FastAPI Backend
        ↓
Data Storage (SQLite/PostgreSQL)
        ↓
ML Forecasting Engine
        ↓
Risk Classification Engine
        ↓
React Monitoring Dashboard
⚙️ Tech Stack
Backend

Python

FastAPI

Scikit-learn

APScheduler

SQLAlchemy

Frontend

React.js

Recharts

Axios

Database

SQLite / PostgreSQL

Data Sources

NOAA Buoy Historical Dataset

NOAA Real-time Buoy Data Feed

📁 Project Structure
ocean-forecasting-system
│
├── backend
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── models
│   │   ├── train_model.py
│   │   ├── forecast_model.pkl
│   │   └── db_models.py
│   │
│   ├── services
│   │   ├── preprocessing.py
│   │   ├── forecasting.py
│   │   ├── live_fetch.py
│   │   ├── scheduler.py
│   │   └── risk_engine.py
│   │
│   ├── routes
│   │   ├── live.py
│   │   ├── forecast.py
│   │   └── history.py
│   │
│   └── data
│       └── historical.csv
│
├── frontend
│   ├── components
│   ├── pages
│   ├── api.js
│   └── App.jsx
│
└── README.md
🚀 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/ocean-forecasting-system.git
cd ocean-forecasting-system
2️⃣ Setup Backend
cd backend
pip install -r requirements.txt

Run the backend server:

uvicorn main:app --reload

Backend will start at:

http://localhost:8000

API documentation:

http://localhost:8000/docs
3️⃣ Setup Frontend
cd frontend
npm install
npm run dev

Frontend will start at:

http://localhost:5173
🧠 Machine Learning Model

The system uses a Random Forest Regression model trained on historical buoy datasets to forecast wave heights.

Input Features

Wind Speed

Air Pressure

Previous Wave Height (Lag Feature)

Target

Wave Height

The trained model predicts future wave conditions and helps determine coastal risk levels.

🔄 Real-Time Data Integration

The system fetches live ocean data from NOAA buoy stations.

Example live data source:

https://www.ndbc.noaa.gov/data/realtime2/46042.txt

A background scheduler automatically fetches new data every 10 minutes, stores it in the database, and updates predictions.

📊 Dashboard

The React dashboard displays:

Current wave height

Wind speed

Risk level indicator

Historical wave trend graph

Predicted wave height

Data updates automatically using API calls.

⚠ Risk Classification Logic
Wave Height < 2m → Low Risk
Wave Height 2m – 4m → Medium Risk
Wave Height > 4m → High Risk
🌍 Applications

Coastal monitoring

Maritime navigation safety

Ocean research

Disaster preparedness

Marine environmental monitoring

🔮 Future Improvements

Deep learning time-series models (LSTM)

Multi-buoy data integration

Advanced anomaly detection

Real-time alert system

Mobile monitoring application

👨‍💻 Contributors

Project developed as part of an AI-driven ocean intelligence system for predictive coastal monitoring.
