from sqlalchemy.orm import Session
from db.schemas.message import MessageCreate, MessageResponse
from db.models.message import Message
from datetime import datetime

def create_message(db: Session, message=MessageCreate):
    db_message = Message(text=message.text,
                         sender_id=message.sender_id,
                         conversation_id=message.conversation_id,
                         time_message= datetime.now().time(),
                         is_from_chatbot=message.is_from_chatbot)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_message_sender(db: Session, sender_id : int,  message=MessageResponse):
   return db.query(Message).filter(Message.sender_id == sender_id).all()

def get_message_conversation(db:Session, conversation_id: int, message=MessageResponse):
    return db.query(Message).filter(Message.conversation_id == conversation_id).all()
 