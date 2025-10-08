# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.base import Base
from db.session import engine 
from db.models import user

#Crea tablas automaitcamente al inicaira
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creando tablas si no existen...")
    Base.metadata.create_all(bind=engine)
    print("Tablas listas")
    yield
    print("Servidor detenido")
    
    
app = FastAPI(
    title = "Trackify API",
    version = "0.1.0",
    descripcion = "API base de Trackify con FastAPI",
    lifespan=lifespan,
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Trackify API"}