from sqlalchemy import Column, Integer, String, ForeignKey, Time, Boolean
from sqlalchemy.orm import relationship
from db.database import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    
    #mensagem chatbot
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=True) 
    is_from_chatbot = Column(Boolean, default=False)
    
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    time_message = Column(Time, nullable=False)


    conversation = relationship("Conversation", back_populates="messages")
