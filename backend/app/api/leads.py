"""Lead management and AI scoring endpoints."""
from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
import random

router = APIRouter()

class LeadSource(str, Enum): WEBSITE="website";WECHAT="wechat";SOCIAL_MEDIA="social_media"
class LeadStatus(str, Enum): NEW="new";CONTACTED="contacted";QUALIFIED="qualified";WON="won";LOST="lost"
class LeadCreate(BaseModel):
    name: str; company: str = ""; phone: str = ""; email: str = ""; source: LeadSource = LeadSource.WEBSITE; notes: str = ""
class LeadResp(BaseModel):
    id: int; name: str; company: str; source: LeadSource; status: LeadStatus; score: float = 0.0; score_label: str = ""; assigned_to: Optional[str] = None; created_at: str
class ScoreDetail(BaseModel):
    lead_id: int; total_score: float; dimensions: dict; recommendation: str

@router.post("/",response_model=LeadResp)
async def create_lead(lead: LeadCreate):
    score = round(random.uniform(30,95),1)
    label = "高意向" if score>=70 else "中意向" if score>=40 else "低意向"
    return LeadResp(id=1,name=lead.name,company=lead.company or "未知公司",source=lead.source,status=LeadStatus.NEW,score=score,score_label=label,created_at=datetime.utcnow().isoformat())

@router.get("/",response_model=List[LeadResp])
async def list_leads(skip:int=0,limit:int=20):
    return [LeadResp(id=i,name=f"客户_{i}",company="某某科技有限公司",source=LeadSource.WEBSITE if i%2==0 else LeadSource.WECHAT,status=LeadStatus.NEW if i<5 else LeadStatus.CONTACTED,score=round(40+i*5,1),score_label="高意向" if i>3 else "中意向",created_at="2025-01-10T10:00:00Z")for i in range(skip+1,skip+limit+1)]

@router.get("/{lid}/score",response_model=ScoreDetail)
async def get_score(lid:int):
    return ScoreDetail(lead_id=lid,total_score=78.5,dimensions={"行业匹配度":85.0,"互动活跃度":72.0,"预算匹配度":80.0},recommendation="高意向客户，建议优先跟进。")

@router.post("/{lid}/assign")
async def assign(lid:int,user_id:str):
    return {"message":f"Lead {lid} assigned to {user_id}"}
