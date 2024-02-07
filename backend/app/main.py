"""ReAgent Backend Application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.api.router import router

app = FastAPI(title="ReAgent API",description="重构智能 AI 自动化营销系统后端 API",version=settings.VERSION,docs_url="/api/docs",redoc_url="/api/redoc")
app.add_middleware(CORSMiddleware,allow_origins=settings.CORS_ORIGINS,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(router,prefix="/api/v1")

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    print(f"[ReAgent] Server started. Version: {settings.VERSION}")

@app.on_event("shutdown")
async def shutdown():
    pass

@app.get("/health")
async def health_check():
    return {"status":"ok","version":settings.VERSION}
