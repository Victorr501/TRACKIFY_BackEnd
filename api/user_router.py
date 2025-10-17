from api.base_router import BaseRouter
from services.user_service import UserService
from db.models.user import User
from db.session import get_db
from schemas.user_schema import UserCreate, UserUpdate, UserRead, UserPasswordUpdate, UserDelete
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.dependencies import get_current_user

user_service = UserService()
user_router = BaseRouter[User, UserCreate, UserUpdate, UserRead](
    service=user_service,
    model_name="users",
    read_schema=UserRead,
    create_schema=UserCreate,
    update_schema=UserUpdate
    
).router

@user_router.put("/{user_id}/password")
def change_user_password(user_id: int, data: UserPasswordUpdate, db: Session = Depends(get_db)):
    user = user_service.change_password(db, user_id, data.old_password, data.new_password)
    return user

@user_router.delete("/{user_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, data: UserDelete, db: Session = Depends(get_db)):
    ok = user_service.delete_user(db, user_id, data.password)
    if not ok:
        raise HTTPException(status_code=400, detail="Contraseña incorrecta o usuario no encontrado")