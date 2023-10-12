from fastapi import FastAPI
from starlette.responses import JSONResponse
from joblib import load
import pandas as pd

app = FastAPI()
predict_pipe = load('amla2/models/predictive/pred_best_model.joblib')
forecast_pipe = load('amla2/models/forecasting/f_model.pkl')

def format_features(
    item_id: str,
    store_id: str,
    date: str):
    date = date.astype('int64')// 10**9
    return {
        'item_id': [item_id],
        'store_id': [store_id],
        'date': [date]
    }

@app.get("/")
def read_root():
    return "Project Objectives"


@app.get('/health', status_code=200)
def healthcheck():
    return 'Project is all ready to go!'

@app.get("/sales/national/")
def forecast_sales(date: str):
    return "Project Objectives"

@app.get("/sales/stores/items/")
def predict_sales(item_id: str, store_id:str, date:str):
    features = format_features(
    item_id,
    store_id,
    date)
    obs = pd.DataFrame(features)
    pred = predict_pipe.predict(obs)
    return JSONResponse(pred.tolist())
