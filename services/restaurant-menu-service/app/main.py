from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Restaurants and menus")

@app.get("/data")
def get_data():
    return {"service":"order-service", "datetime":datetime.now()}

@app.get("/number")
def get_number():
    return 42
