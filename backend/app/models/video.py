from sqlalchemy import Column,Integer,String,Boolean,DateTime,Text,JSON
from backend.app.core.database import Base
from datetime import datetime

class Video(Base):
    __tablename__="videos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(200),nullable=False)
    description=Column(Text,default="")
    script=Column(Text)
    status=Column(String(20),default="draft")
    platforms=Column(JSON,default=["douyin"])
    ai_voice=Column(String(50),default="xiaoyan")
    auto_subtitle=Column(Boolean,default=True)
    views=Column(Integer,default=0);likes=Column(Integer,default=0)
    user_id=Column(Integer,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)
    published_at=Column(DateTime,nullable=True)
