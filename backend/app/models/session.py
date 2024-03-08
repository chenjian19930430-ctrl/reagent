from sqlalchemy import Column,Integer,String,DateTime,JSON
from backend.app.core.database import Base
from datetime import datetime

class ChatSession(Base):
    __tablename__="chat_sessions"
    id=Column(Integer,primary_key=True,index=True)
    session_id=Column(String(50),unique=True,nullable=False,index=True)
    user_name=Column(String(100))
    status=Column(String(20),default="active")
    messages=Column(JSON,default=[])
    created_at=Column(DateTime,default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
