from sqlalchemy import Column,Integer,String,Float,DateTime,Text
from backend.app.core.database import Base
from datetime import datetime

class Lead(Base):
    __tablename__="leads"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    company=Column(String(200),default="")
    phone=Column(String(20));email=Column(String(120))
    source=Column(String(20),default="website")
    status=Column(String(20),default="new")
    score=Column(Float,default=0.0)
    assigned_to=Column(Integer,nullable=True)
    notes=Column(Text,default="")
    created_at=Column(DateTime,default=datetime.utcnow)
