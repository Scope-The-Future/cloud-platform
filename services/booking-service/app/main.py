from fastapi import FastAPI

app = FastAPI(title="<имя-сервиса>")


@app.get("/health")
def health():
    # Проверка, что сервис жив (пригодится для healthcheck позже)
    return {"status": "ok"}


@app.get("/data")
def get_data():
    return {"service": "<имя-сервиса>", "message": "Привет"}