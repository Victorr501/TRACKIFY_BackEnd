from datetime import timedelta
from typing import Optional
from sqlalchemy.orm import Session
from core.security import verify_password, get_password_hash, create_access_token, decode_access_token
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate
from fastapi import HTTPException
from datetime import datetime
from schemas.user_schema import UserUpdate

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()
        
    def register_user(self, db: Session, username: str, email: str, password: str, fcm_token: Optional[str] = None ):
        existing = self.user_repo.get_by_email(db, email)
        if existing:
            raise ValueError("Email already registered")
        
        hashed_password = get_password_hash(password)
        user_data = UserCreate(username=username, email= email, password= hashed_password, fcm_token=fcm_token)
        return self.user_repo.create(db,user_data)
    
    def authenticate_user(self, db: Session, email: str, password: str, fcm_token: Optional[str] = None ):
        user = self.user_repo.get_by_email(db, email)
        if not user or not verify_password(password, user.password):
            return None
        update_user = UserUpdate(is_active=True, last_login=datetime.utcnow())
        
        if fcm_token and fcm_token != getattr(user, "fcm_token", None):
            update_user.fcm_token = fcm_token
        
        user = self.user_repo.update(db, user, update_user)
        return user
    
    def generate_token(self, user_id: int, username: str):
        token_data = {"sub": str(user_id), "username": username}
        return create_access_token(token_data, expires_delta = timedelta(days=1))
    
    def logout_user(self, db: Session, token: str):
        payload = decode_access_token(token)
        if not payload or "sub" not in payload:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")
        
        user_id = int(payload["sub"])
        user = self.user_repo.get(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        update_user = UserUpdate(is_active=False, last_login=datetime.utcnow())

        
        return self.user_repo.update(db, user, update_user)