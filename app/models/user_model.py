from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, true
from core.database import Base
from datetime import datetime

from ..utils.enum import userType


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username=Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    userType= Column(Enum(userType),default=userType.user,nullable=True)
    image=Column(String, nullable=True)
    createdAt = Column(DateTime, default=datetime.utcnow)   # auto insert
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)# auto update
