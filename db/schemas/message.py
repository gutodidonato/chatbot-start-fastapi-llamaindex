from pydantic import BaseModel
from datetime import time
from typing import Optional
    
class MessageBase(BaseModel):
    text: str
    time_message: time
    sender_id: int
    conversation_id: int
    is_from_chatbot: bool
    
class MessageCreate(MessageBase):
    pass  

class MessageResponse(MessageBase):
    id: int
    conversation_name: Optional[str] 
    sender_name: Optional[str]  

    class Config:
        orm_mode = True