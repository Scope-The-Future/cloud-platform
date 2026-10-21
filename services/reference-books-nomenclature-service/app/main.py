from fastapi import FastAPI

app = FastAPI(title="reference-books-nomenclature-service")


@app.get("/health")
def health():
    # Проверка, что сервис жив (пригодится для healthcheck позже)
    return {"status": "ok"}


@app.get("/data")
def get_data():
    return {"service": "reference-books-nomenclature-service", "message": "Привет"}