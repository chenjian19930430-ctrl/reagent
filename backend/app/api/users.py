"""User management endpoints."""
from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str; email: str; password: str; role: str = "user"
class UserResp(BaseModel):
    id: int; username: str; email: str; role: str; is_active: bool; created_at: str

@router.post("/",response_model=UserResp)
async def create_user(user: UserCreate):
    return UserResp(id=1,username=user.username,email=user.email,role=user.role,is_active=True,created_at="2024-02-15T10:00:00Z")

@router.get("/{uid}",response_model=UserResp)
async def get_user(uid: int):
    return UserResp(id=uid,username="demo_user",email="demo@example.com",role="user",is_active=True,created_at="2024-02-15T10:00:00Z")

@router.put("/{uid}",response_model=UserResp)
async def update_user(uid: int, user: UserCreate):
    return UserResp(id=uid,username=user.username,email=user.email,role=user.role,is_active=True,created_at="2024-02-15T10:00:00Z")

@router.delete("/{uid}")
async def delete_user(uid: int):
    return {"message":f"User {uid} deleted successfully"}
