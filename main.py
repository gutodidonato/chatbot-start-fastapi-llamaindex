from fastapi import FastAPI
from db.database import engine, Base
import db.models
from routes import user

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(user.router)