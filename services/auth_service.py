from datetime import timedelta
from sqlalchemy.orm import Session
from core.security import verify_password, get_password_hash, create_access_token
from repositories.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()
        
    def register_user(self, db: Session, username: str, email: str, password: str):
        existing = self.user_repo.get_by_email(db, email)
        if existing:
            raise ValueError("Email already registered")
        
        hashed_password = get_password_hash(password)
        user_data = {"username": username, "email": email, "password_hash": hashed_password}
        return self.user_repo.create(db, type("UserCreate", (), user_data))
    
    def authenticate_user(self, db: Session, email: str, password: str):
        user = self.user_repo.get_by_email(db, email)
        if not user or not verify_password(password, user.password_hash):
            return None
        return user
    
    def generate_token(self, user_id: int, username: str):
        token_data = {"sub": str(user_id), "username": username}
        return create_access_token(token_data, expirex_delta = timedelta(days=1))
    