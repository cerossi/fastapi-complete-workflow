"""
Configuração do banco de dados.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from app.config import get_settings

settings = get_settings()

# Criar engine do SQLAlchemy
engine = create_engine(
    settings.database_url,
    echo=settings.database_echo,
    pool_size=settings.database_pool_size,
    max_overflow=settings.database_max_overflow,
    connect_args={"check_same_thread": False}
    if "sqlite" in settings.database_url
    else {},
)

# Criar session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()


def get_db() -> Session:
    """
    Dependência para obter sessão do banco de dados.

    Yields:
        Session: Sessão do banco de dados
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
