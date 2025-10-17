from services.base_service import BaseService
from repositories.user_repository import UserRepository
from db.models.user import User
from schemas.user_schema import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from core.security import verify_password, get_password_hash

class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self):
        respository = UserRepository()
        super().__init__(UserRepository())
        
    def get_by_email(self, db: Session, email: str):
        return self.repository.get_by_email(db, email)
    
    def change_password(self, db: Session, user_id: int, old_password: str, new_password: str):
        userdb = self.repository.get(db, user_id)
        if not verify_password(old_password, userdb.password):
            return None
        
        password_hash = get_password_hash(new_password)
        user = self.repository.change_password(db,user_id, password_hash)
        
        return user