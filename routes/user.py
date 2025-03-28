from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.schemas.user import UserCreate, UserResponse
from db.crud.user import get_user_by_login, get_user, create_user, login_user
from db import database

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def begin_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_login(db, user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="Login já cadastrado")
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user

@router.post("/login", response_model=UserResponse)
def do_login_user(login: str, password: str, db: Session = Depends(get_db)):
    db_user = login_user(login=login, password=password, db=db)
    if not db_user:
        raise HTTPException(status_code=400, detail="Credenciais inválidas!")
    return db_user
    