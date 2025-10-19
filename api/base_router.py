from fastapi import APIRouter, Body, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import Generic, TypeVar, Type, List
from db.session import get_db
from services.base_service import BaseService
from pydantic import BaseModel
from db.base import Base
from core.dependencies import get_current_user

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)

class BaseRouter(Generic[ModelType, CreateSchemaType, UpdateSchemaType, ReadSchemaType]):
    def __init__(
        self, 
        service: BaseService, 
        model_name: str,
        read_schema: Type[ReadSchemaType],
        create_schema: Type[CreateSchemaType],
        update_schema: Type[UpdateSchemaType],):
        self.router = APIRouter(
            prefix=f"/{model_name}", 
            tags=[model_name.capitalize()],
            dependencies=[Depends(get_current_user)]
        )
        
        self.service = service
        self.read_schema = read_schema
        self.create_schema = create_schema
        self.update_schema = update_schema

        @self.router.get("/{item_id}", response_model=ReadSchemaType)
        def get_one(item_id: int, db: Session = Depends(get_db)):
            obj = self.service.get(db, item_id)
            if not obj:
                raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
            return self.read_schema.model_validate(obj)
        
        
        @self.router.get("/", response_model=List[ReadSchemaType])
        def get_all(db: Session = Depends(get_db)):
            obj = self.service.get_all(db)
            return self.read_schema.model_validate(obj)
        
        @self.router.post("/", response_model=ReadSchemaType)
        def create(request_body: dict = Body(...), db: Session = Depends(get_db)):
            data = request_body.model_dump() if isinstance(request_body, BaseModel) else request_body
            item = self.create_schema(**data)
            obj =  self.service.create(db, item)
            return self.read_schema.model_validate(obj, from_attributes=True)
        
        @self.router.put("/{item_id}", response_model=ReadSchemaType)
        def update(item_id: int, item: dict = Body(...), db: Session = Depends(get_db)):
            validated_item = self.update_schema.model_validate(item)
            print(validated_item)
            update = self.service.update(db, item_id, validated_item)
            if not update:
                raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
            return self.read_schema.model_validate(update)
        
        @self.router.delete("/{item_id}")
        def delete(item_id: int, db: Session = Depends(get_db)):
            deleted = self.service.delete(db, item_id)
            if not delete:
                raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
            return {"message" : f"{model_name.capitalize()} deleted succesfully"}
        
        