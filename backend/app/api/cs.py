"""AI Customer Service endpoints."""
from fastapi import APIRouter, Request
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class MsgReq(BaseModel):
    session_id: str; content: str
class MsgResp(BaseModel):
    session_id: str; reply: str; confidence: float = 1.0; suggested_actions: List[str] = []; created_at: str

@router.post("/messages",response_model=MsgResp)
async def send_message(msg: MsgReq):
    return MsgResp(session_id=msg.session_id,reply=f"您好！我是AI客服助手。关于「{msg.content}」的问题，我来为您解答：",confidence=0.95,suggested_actions=["了解定价","预约演示","联系销售"],created_at=datetime.utcnow().isoformat())

@router.get("/sessions",response_model=List[dict])
async def list_sessions():
    return [{"session_id":"s1","user_name":"王经理","status":"active","last_message":"请问定价方案？"},{"session_id":"s2","user_name":"李总","status":"closed"}]

@router.get("/knowledge-base",response_model=List[dict])
async def search_knowledge():
    return [{"id":1,"question":"支持哪些短视频平台？","answer":"支持抖音、快手、小红书、视频号","category":"product","hit_count":156}]

@router.post("/wechat/callback")
async def wechat_callback(request: Request):
    body = await request.json()
    return {"errcode":0,"errmsg":"ok"}
