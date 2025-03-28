from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship
from db.database import Base



class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ia_id = Column(Integer, ForeignKey("ias.id"))

    user = relationship("User", back_populates="conversations")
    ia = relationship("Agent", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")

