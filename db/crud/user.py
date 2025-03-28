from sqlalchemy.orm import Session
from db.schemas.user import UserCreate, UserResponse
from passlib.context import CryptContext
from db.models.user import User

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_login(db: Session, login: str):
    return db.query(User).filter(User.login == login).first()

def login_user(db: Session, login: str, password : str):
    user = db.query(User).filter(User.login == login).first()
    if user is None:
        return None  
    if pwd_context.verify(password, user.password):
        return user 
    else:
        return None 

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(name=user.name, job=user.job, login=user.login, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
