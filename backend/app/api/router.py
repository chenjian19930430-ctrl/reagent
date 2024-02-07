"""API routing registration."""
from fastapi import APIRouter
from app.api import auth, users, videos, marketing, cs, leads, documents, health

router = APIRouter()
router.include_router(health.router,prefix="/health",tags=["health"])
router.include_router(auth.router,prefix="/auth",tags=["auth"])
router.include_router(users.router,prefix="/users",tags=["users"])
router.include_router(videos.router,prefix="/videos",tags=["videos"])
router.include_router(marketing.router,prefix="/marketing",tags=["marketing"])
router.include_router(cs.router,prefix="/cs",tags=["customer-service"])
router.include_router(leads.router,prefix="/leads",tags=["leads"])
router.include_router(documents.router,prefix="/documents",tags=["documents"])
