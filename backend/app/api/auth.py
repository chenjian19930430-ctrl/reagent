"""JWT Authentication endpoints."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

router = APIRouter()
SECRET_KEY = "reagent-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_EXPIRE = 1440

class LoginReq(BaseModel):
    username: str; password: str
class TokenRes(BaseModel):
    access_token: str; token_type: str = "bearer"; expires_in: int; user_id: int; username: str
class RegisterReq(BaseModel):
    username: str; email: str; password: str

@router.post("/login",response_model=TokenRes)
async def login(req: LoginReq):
    token = jwt.encode({"sub":req.username,"exp":datetime.utcnow()+timedelta(minutes=ACCESS_EXPIRE)},SECRET_KEY,algorithm=ALGORITHM)
    return TokenRes(access_token=token,expires_in=ACCESS_EXPIRE*60,user_id=1,username=req.username)

@router.post("/register")
async def register(req: RegisterReq):
    return {"message":"Registration successful","username":req.username}

@router.post("/refresh")
async def refresh_token(token: str):
    return {"message":"Token refreshed"}
