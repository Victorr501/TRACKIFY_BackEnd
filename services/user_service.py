from services.base_service import BaseService
from repositories.user_repository import UserRepository
from db.models.user import User
from schemas.user_schema import UserCreate, UserUpdate
from sqlalchemy.orm import Session

class UserService(BaseService[User, UserCreate, UserCreate]):
    def __init__(self):
        super().__init__(UserRepository())
        
    