#!/usr/bin/env python3
"""Initialize database."""
import sys; sys.path.insert(0,".")
from backend.app.core.database import engine, Base
from backend.app.models.user import User
from backend.app.models.video import Video
from backend.app.models.lead import Lead
from backend.app.models.session import ChatSession
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")
