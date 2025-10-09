from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Generic, TypeVar, Type, List
from db.session import get_db
from services.base_service import BaseService
from pydantic import BaseModel
from db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)

class BaseRouter(Generic[ModelType, CreateSchemaType, UpdateSchemaType, ReadSchemaType]):
    def __init__(self, service: BaseService, model_name: str ):
        self.router = APIRouter(prefix=f"/{model_name}", tags=[model_name.capitalize()])
        self.service = service

        @self.router.get("/{item_id}", response_model=ReadSchemaType)
        def get_one(item_id: int, db: Session = Depends(get_db)):
            obj = self.service.get(db, item_id)
            if not obj:
                raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
            return obj
        
        @self.router.get("/", response_model=List[ReadSchemaType])
        def get_all(db: Session = Depends(get_db)):
            return self.service.get_all(db)
        
        @self.router.post("/", response_model=ReadSchemaType)
        def create(item: CreateSchemaType, db: Session = Depends(get_db)):
            return self.service.create(db, item)
        
        @self.router.put("/{item_id}", response_model=ReadSchemaType)
        def update(item_id: int, item: UpdateSchemaType, db: Session = Depends(get_all)):
            update = self.service.update(db, item_id, item)
            if not update:
                raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
            return update
        
        @self.router.delete("/{item_id}")
        def delete(item_id: int, db: Session = Depends(get_db)):
            deleted = self.service.delete(db, item_id)
            if not delete:
                raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
            return {"message" : f"{model_name.capitalize()} deleted succesfully"}
        
        