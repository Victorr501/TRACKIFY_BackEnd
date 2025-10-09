from sqlalchemy.orm import Session
from typing import Generic, TypeVar, Type, List, Optional
from pydantic import BaseModel
from db.base import Base

ModelType = TypeVar("ModelType", bound=Base) 
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        
    def get(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()
    
    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        for key, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def delete(self, db: Session, id: int) -> bool:
        obj = db.query(self.model).filter(self.model.id == id).first()
        if not obj:
            return False
        db.delete(obj)
        db.commit()
        return True
    
    
        