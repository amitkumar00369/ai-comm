from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import logging
from core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

# ✅ GLOBAL (IMPORTANT)
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def connect_db():
    try:
        with engine.connect() as conn:
            logger.info(f"✅ Database connected successfully: {DATABASE_URL}")
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")