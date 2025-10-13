from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository
from db.base import Base
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, repository: BaseRepository):
        self.repository = repository
        
    def get(self, db: Session, id: int) -> Optional[ModelType]:
        return self.repository.get(db, id)
    
    def get_all(self, db: Session) -> List[ModelType]:
        return self.repository.get_all(db)
    
    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        return self.repository.create(db, obj_in)
    
    def update(self, db: Session, id: int, obj_in: UpdateSchemaType) -> Optional[ModelType]:
        db_obj = self.repository.get(db, id)
        if not db_obj:
            return None
        return self.repository.update(db, db_obj, obj_in)
    
    def delete(self, db:Session, id: int ) -> bool:
        return self.repository.delete(db, id)
        