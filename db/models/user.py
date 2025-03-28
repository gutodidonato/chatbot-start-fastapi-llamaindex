from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    job = Column(String, nullable=False)
    login = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    conversations = relationship("Conversation", back_populates="user")


class Agent(Base):
    __tablename__ = "ias"
    
    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, nullable=False)

    conversations = relationship("Conversation", back_populates="ia")


class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ia_id = Column(Integer, ForeignKey("ias.id"))

    user = relationship("User", back_populates="conversations")
    ia = relationship("Agent", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")


class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id")) 
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    time_message = Column(Time, nullable=False)

    conversation = relationship("Conversation", back_populates="messages")
