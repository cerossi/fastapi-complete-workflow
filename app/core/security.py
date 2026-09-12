"""
Utilitários de segurança e autenticação JWT.
"""

from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.config import get_settings

# Configurar contexto de criptografia
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class TokenData(BaseModel):
    """Dados do token JWT."""

    sub: str  # Subject (user_id)
    exp: datetime  # Expiração
    iat: datetime  # Emitido em
    type: str = "access"  # Tipo de token


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verificar se a senha corresponde ao hash.

    Args:
        plain_password: Senha em texto plano
        hashed_password: Senha hasheada

    Returns:
        bool: True se a senha está correta
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Gerar hash seguro de uma senha.

    Args:
        password: Senha em texto plano

    Returns:
        str: Senha hasheada
    """
    return pwd_context.hash(password)


def create_access_token(
    data: dict[str, Any],
    expires_delta: Optional[timedelta] = None,
) -> str:
    """
    Criar token de acesso JWT.

    Args:
        data: Dados a serem codificados no token
        expires_delta: Tempo de expiração customizado

    Returns:
        str: Token JWT codificado
    """
    settings = get_settings()
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.access_token_expire_minutes
        )

    to_encode.update({"exp": expire, "type": "access"})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    return encoded_jwt


def create_refresh_token(data: dict[str, Any]) -> str:
    """
    Criar token de refresh JWT.

    Args:
        data: Dados a serem codificados no token

    Returns:
        str: Token JWT de refresh codificado
    """
    settings = get_settings()
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.refresh_token_expire_days
    )

    to_encode.update({"exp": expire, "type": "refresh"})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    return encoded_jwt


def verify_token(token: str, token_type: str = "access") -> Optional[TokenData]:
    """
    Verificar e decodificar token JWT.

    Args:
        token: Token JWT a ser verificado
        token_type: Tipo de token esperado (access ou refresh)

    Returns:
        Optional[TokenData]: Dados do token se válido, None caso contrário
    """
    settings = get_settings()

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )

        user_id: Optional[str] = payload.get("sub")
        token_type_check: Optional[str] = payload.get("type")

        if user_id is None or token_type_check != token_type:
            return None

        return TokenData(
            sub=user_id,
            exp=datetime.fromtimestamp(payload["exp"], tz=timezone.utc),
            iat=datetime.fromtimestamp(payload["iat"], tz=timezone.utc),
            type=token_type_check,
        )

    except JWTError:
        return None
