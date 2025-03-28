from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship
from db.database import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id")) 
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    time_message = Column(Time, nullable=False)

    conversation = relationship("Conversation", back_populates="messages")
