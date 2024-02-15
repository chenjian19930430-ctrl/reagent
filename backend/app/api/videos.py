"""Video management and publishing endpoints."""
from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import random

router = APIRouter()

class VideoCreate(BaseModel):
    title: str; description: str = ""; script: str; platforms: List[str] = ["douyin"]; ai_voice: str = "xiaoyan"; auto_subtitle: bool = True
class VideoResp(BaseModel):
    id: int; title: str; status: str; platforms: List[str]; created_at: str; views: int = 0; likes: int = 0

@router.post("/",response_model=VideoResp)
async def create_video(v: VideoCreate):
    return VideoResp(id=1,title=v.title,status="processing",platforms=v.platforms,created_at=datetime.utcnow().isoformat())

@router.get("/",response_model=List[VideoResp])
async def list_videos(skip: int = 0, limit: int = 20):
    return [VideoResp(id=i,title=f"营销视频 #{i}",status="published"if i%2==0 else"draft",platforms=["douyin","kuaishou"]if i%3==0 else["douyin"],created_at="2024-06-15T10:00:00Z",views=random.randint(100,10000),likes=random.randint(10,500))for i in range(skip+1,skip+limit+1)]

@router.post("/{vid}/publish")
async def publish_video(vid: int):
    return {"message":f"Video {vid} publishing","status":"publishing"}
