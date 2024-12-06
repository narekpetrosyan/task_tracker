from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
