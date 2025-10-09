# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.base import Base
from db.session import engine 
from db.models import user, habits, habit_log, reminder
from api.user_router import user_router
from api.habit_router import habit_router
from api.habit_log_router import habit_log_router
from api.reminder_router import reminder_router
from api.auth_router import router as auth_router

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

#Registrar rutasd
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(habit_router)
app.include_router(habit_log_router)
app.include_router(reminder_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Trackify API"}