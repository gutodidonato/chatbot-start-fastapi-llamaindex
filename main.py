from fastapi import FastAPI
from db.database import engine, Base
import db.models
from routes import user, message

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(user.router)
app.include_router(message.router)