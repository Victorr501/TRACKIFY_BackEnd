from services.base_service import BaseService
from repositories.user_repository import UserRepository
from db.models.user import User
from schemas.user_schema import UserCreate, UserUpdate
from sqlalchemy.orm import Session

class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self):
        respository = UserRepository()
        super().__init__(UserRepository())
        
    def get_by_email(self, db: Session, email: str):
        return self.repository.get_by_email(db, email)