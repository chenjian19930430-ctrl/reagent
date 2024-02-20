"""AI document generation endpoints."""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class DocCreate(BaseModel):
    title: str; doc_type: str; variables: dict = {}
class DocResp(BaseModel):
    id: int; title: str; doc_type: str; status: str; created_at: str; word_count: int = 0
class MinutesInput(BaseModel):
    title: str; date: str; participants: List[str]; recording_text: str

@router.post("/",response_model=DocResp)
async def create_doc(d: DocCreate):
    return DocResp(id=1,title=d.title,doc_type=d.doc_type,status="completed",created_at=datetime.utcnow().isoformat(),word_count=1500)

@router.post("/meeting-minutes",response_model=DocResp)
async def minutes(m: MinutesInput):
    return DocResp(id=2,title=m.title,doc_type="meeting_minutes",status="completed",created_at=datetime.utcnow().isoformat(),word_count=800)

@router.get("/",response_model=List[DocResp])
async def list_docs():
    return [DocResp(id=1,title="Q4 营销效果分析报告",doc_type="report",status="completed",created_at="2025-10-10T09:00:00Z",word_count=3500)]
