"""
Exceções personalizadas da aplicação.
"""


class APIException(Exception):
    """Exceção base da API."""

    def __init__(self, message: str, status_code: int = 500, detail: str | None = None):
        """
        Inicializar exceção.

        Args:
            message: Mensagem de erro
            status_code: Código HTTP da resposta
            detail: Detalhes adicionais do erro
        """
        self.message = message
        self.status_code = status_code
        self.detail = detail or message
        super().__init__(self.message)


class ValidationError(APIException):
    """Erro de validação."""

    def __init__(self, message: str, detail: str | None = None):
        """
        Inicializar erro de validação.

        Args:
            message: Mensagem de erro
            detail: Detalhes do erro
        """
        super().__init__(message, status_code=422, detail=detail)


class NotFoundError(APIException):
    """Recurso não encontrado."""

    def __init__(self, resource: str):
        """
        Inicializar erro de não encontrado.

        Args:
            resource: Nome do recurso não encontrado
        """
        super().__init__(
            f"{resource} não encontrado",
            status_code=404,
            detail=f"O recurso {resource} solicitado não foi encontrado",
        )


class UnauthorizedError(APIException):
    """Erro de autenticação."""

    def __init__(self, message: str = "Não autenticado"):
        """
        Inicializar erro de autenticação.

        Args:
            message: Mensagem de erro
        """
        super().__init__(message, status_code=401)


class ForbiddenError(APIException):
    """Erro de permissão."""

    def __init__(self, message: str = "Acesso proibido"):
        """
        Inicializar erro de permissão.

        Args:
            message: Mensagem de erro
        """
        super().__init__(message, status_code=403)


class ConflictError(APIException):
    """Erro de conflito."""

    def __init__(self, message: str):
        """
        Inicializar erro de conflito.

        Args:
            message: Mensagem de erro
        """
        super().__init__(message, status_code=409)


class InternalServerError(APIException):
    """Erro interno do servidor."""

    def __init__(self, message: str = "Erro interno do servidor"):
        """
        Inicializar erro interno.

        Args:
            message: Mensagem de erro
        """
        super().__init__(message, status_code=500)
