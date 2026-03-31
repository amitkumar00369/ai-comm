from fastapi import FastAPI
from core.database import connect_db,Base,engine,SessionLocal
from core.config import settings
import app.models
from fastapi import FastAPI,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from fastapi.security import HTTPBearer
from starlette.staticfiles import StaticFiles
import os
# from src.routes.private import userPrivateRouter
from app.middleware.auth_middleware import jwt_auth
# from .routes.common import commonRouter
# from .routes.route import MlRouter
# from .config.db import Base,engine
from app.api.v1.routes_users import userRouter
security = HTTPBearer()

app = FastAPI()

import multiprocessing

@app.on_event("startup")
def startup():
    if multiprocessing.current_process().name == "MainProcess":
        connect_db()
        Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")

app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads")
# CORS
# app.["UPLOAD_FOLDER"] = "uploads"

# 👇 THIS LINE IS THE KEY

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
# app.include_router(commonRouter,prefix="/api",tags = ["File-Upload"])
# app.include_router(MlRouter, prefix="/api/ml", tags=["ML-API"])
app.include_router(userRouter, prefix="/api/user", tags=["User-API"])
# app.include_router(userPrivateRouter, prefix="/api/user/private", tags=["User-Private-API"], dependencies=[Depends(security), Depends(jwt_auth)])
print(f" server runing on port : http://localhost:{settings.PORT}/docs")
