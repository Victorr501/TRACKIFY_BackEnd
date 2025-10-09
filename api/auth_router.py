from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.session import get_db
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])
auth_service = AuthService()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/register")
def register_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    try:
        user = auth_service.register_user(db, username, email, password)
        return {"message": "User registrado perfectamente", "user_id" : user.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")
def login(from_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, from_data.username, from_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth_service.generate_token(user.id, user.username)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    from core.security import decode_access_toke
    data = decode_access_toke(token)
    if not data:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": data}