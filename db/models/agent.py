from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship
from db.database import Base

class Agent(Base):
    __tablename__ = "ias"
    
    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, nullable=False)

    conversations = relationship("Conversation", back_populates="ia")

