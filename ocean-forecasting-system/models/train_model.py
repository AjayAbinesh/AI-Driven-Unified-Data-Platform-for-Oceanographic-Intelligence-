import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from services.preprocessing import clean_dataset

df = pd.read_csv("data/historical.csv", delim_whitespace=True)
df = clean_dataset(df)

features = ["WSPD", "PRES", "lag_1"]
target = "WVHT"

X = df[features]
y = df[target]

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "models/forecast_model.pkl")
print("Model trained and saved.")