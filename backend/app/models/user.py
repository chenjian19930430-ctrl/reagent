from sqlalchemy import Column,Integer,String,Boolean,DateTime
from backend.app.core.database import Base
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,nullable=False,index=True)
    email=Column(String(120),unique=True,nullable=False,index=True)
    hashed_password=Column(String(255),nullable=False)
    role=Column(String(20),default="user")
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
