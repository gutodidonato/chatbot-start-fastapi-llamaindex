from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    job: str
    login: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    job: str
    login: str

    class Config:
        from_attributes = True