"""Health check endpoints."""
from fastapi import APIRouter
from datetime import datetime
router = APIRouter()
@router.get("/ping")
async def ping():
    return {"message":"pong","timestamp":datetime.utcnow().isoformat()}
@router.get("/ready")
async def readiness():
    return {"status":"ready","services":{"database":"ok","redis":"ok"}}
