# app/main.py
from fastapi import FastAPI

app = FastAPI(
    title = "Trackify API",
    version = "0.1.0",
    descripcion = "API base de Trackify con FastAPI"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Trackify API"}