from fastapi import FastAPI
from datetime import datetime
import httpx
import os

app = FastAPI(title="order-service")

RESTAURANT_MENU_SERVICE_URL = os.getenv("RESTAURANT_MENU_SERVICE_URL", "http://localhost:8002")

@app.get("/data")
def get_data():
    return {"service":"order-service", "datetime":datetime.now()}


@app.get("/call-b")
async def call_service_b():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{RESTAURANT_MENU_SERVICE_URL}/number",timeout=5)
            return {
                "sender": "Сервис order",
                "received_from_restaraunt": response.json()
            }
        except Exception as e:
            return {"error": f"Не удалось связаться с restaraunt service: {str(e)}"}