"""Marketing campaign management endpoints."""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class CampaignCreate(BaseModel):
    name: str; description: str = ""; start_date: datetime; end_date: datetime; budget: float = 0.0; channels: List[str] = ["social_media"]
class CampaignResp(BaseModel):
    id: int; name: str; status: str; start_date: str; end_date: str; budget: float; spent: float = 0.0; leads_generated: int = 0; roi: float = 0.0

@router.post("/campaigns",response_model=CampaignResp)
async def create(c: CampaignCreate):
    return CampaignResp(id=1,name=c.name,status="draft",start_date=c.start_date.isoformat(),end_date=c.end_date.isoformat(),budget=c.budget)

@router.get("/campaigns",response_model=List[CampaignResp])
async def list_campaigns():
    return [CampaignResp(id=1,name="Q2 新品推广",status="active",start_date="2025-04-01T00:00:00Z",end_date="2025-06-30T23:59:59Z",budget=50000.0,spent=23500.0,leads_generated=1280,roi=2.8)]

@router.get("/templates",response_model=List[dict])
async def list_templates():
    return [{"id":1,"name":"新品发布海报","category":"social_media","content":"【新品首发】{{product_name}} 正式上线！"},{"id":2,"name":"促销短信","category":"sms","content":"【重构智能】{{discount}} 优惠来了！"}]
