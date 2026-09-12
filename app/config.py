"""
Configuração principal da aplicação FastAPI.
"""

import logging
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações da aplicação."""

    # Aplicação
    app_name: str = "FastAPI Complete Workflow"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = False

    # API
    api_title: str = "FastAPI API"
    api_description: str = "API desenvolvida com FastAPI seguindo melhores práticas"
    api_version: str = "v1"

    # Servidor
    host: str = "0.0.0.0"
    port: int = 8000

    # Banco de Dados
    database_url: str = "sqlite:///./test.db"
    database_echo: bool = False
    database_pool_size: int = 5
    database_max_overflow: int = 10

    # CORS
    cors_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]
    cors_credentials: bool = True
    cors_methods: list[str] = ["*"]
    cors_headers: list[str] = ["*"]

    # JWT
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    class Config:
        """Configurações do Pydantic."""

        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """
    Obter configurações em cache.

    Returns:
        Settings: Instância das configurações
    """
    return Settings()


# Logger configurado
logger = logging.getLogger(__name__)


def configure_logging(settings: Settings) -> None:
    """
    Configurar logging da aplicação.

    Args:
        settings: Instância das configurações
    """
    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logger.info(f"Aplicação iniciada em modo {settings.app_env}")
