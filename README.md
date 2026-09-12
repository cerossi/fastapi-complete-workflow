# Fluxo de Desenvolvimento Completo - API FastAPI

Uma estrutura profissional e production-ready para desenvolvimento de APIs com FastAPI, incluindo melhores práticas de qualidade, segurança e CI/CD.

## 🎯 Características

- ✅ **FastAPI** - Framework moderno e rápido
- ✅ **UV** - Gerenciador de dependências rápido e confiável
- ✅ **Testes Automatizados** - pytest com cobertura de código
- ✅ **CI/CD** - GitHub Actions para automação
- ✅ **Segurança** - Análise estática com Bandit, SAST
- ✅ **Qualidade de Código** - Black, Ruff, mypy, pylint
- ✅ **Documentação** - Swagger automático + MkDocs
- ✅ **Linting Pre-commit** - Validação antes de commits
- ✅ **Database Migrations** - Alembic para versionamento de BD

## 📋 Pré-requisitos

- Python >= 3.11
- UV (https://docs.astral.sh/uv/)
- Git

## 🚀 Início Rápido

### 1. Clonar e configurar o repositório

```bash
git clone https://github.com/cerossi/fastapi-complete-workflow.git
cd fastapi-complete-workflow

# Instalar dependências com UV
uv sync
```

### 2. Configurar variáveis de ambiente

```bash
cp .env.example .env
# Editar .env com suas configurações
```

### 3. Executar a aplicação

```bash
# Desenvolvimento
uv run python -m app.main

# Ou com uvicorn diretamente
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: http://localhost:8000

**Documentação Swagger:** http://localhost:8000/docs

**Documentação ReDoc:** http://localhost:8000/redoc

## 📁 Estrutura do Projeto

```
fastapi-complete-workflow/
├── .github/
│   └── workflows/
│       ├── ci.yml                 # CI/CD pipeline
│       ├── security.yml           # Análise de segurança
│       └── deploy.yml             # Deploy automático (opcional)
├── app/
│   ├── __init__.py
│   ├── main.py                    # Entrada da aplicação
│   ├── config.py                  # Configurações
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/                    # Versão 1 da API
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   └── health.py
│   │   │   └── schemas.py
│   │   └── dependencies.py        # Dependências globais
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py            # JWT, autenticação
│   │   ├── logging.py             # Logging configurado
│   │   └── exceptions.py          # Exceções personalizadas
│   ├── models/
│   │   ├── __init__.py
│   │   └── database.py            # Modelos SQLAlchemy
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py        # Lógica de negócio
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py            # Configuração do banco
│   └── middleware/
│       ├── __init__.py
│       └── cors.py                # CORS e headers de segurança
├── migrations/                    # Alembic migrations
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Fixtures pytest
│   ├── test_main.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_services.py
│   │   └── test_models.py
│   └── integration/
│       ├── __init__.py
│       └── test_endpoints.py
├── docs/                          # Documentação MkDocs
│   ├── index.md
│   ├── getting-started.md
│   ├── api.md
│   └── deployment.md
├── scripts/
│   ├── init_db.py                 # Inicializar banco
│   └── seed.py                    # Seed de dados
├── .env.example                   # Exemplo de variáveis
├── .gitignore
├── .pre-commit-config.yaml        # Pre-commit hooks
├── pyproject.toml                 # Dependências e configurações
├── pytest.ini
├── mkdocs.yml                     # Configuração MkDocs
└── README.md
```

## 🧪 Testes

### Executar todos os testes

```bash
uv run pytest
```

### Com cobertura de código

```bash
uv run pytest --cov=app --cov-report=html
```

### Testes específicos

```bash
# Testes unitários
uv run pytest tests/unit

# Testes de integração
uv run pytest tests/integration

# Modo watch
uv run pytest-watch
```

## 🔍 Qualidade de Código

### Formatação com Black

```bash
uv run black app tests
```

### Linting com Ruff

```bash
uv run ruff check app tests
uv run ruff check app tests --fix  # Auto-fix
```

### Type checking com mypy

```bash
uv run mypy app
```

### Análise com Pylint

```bash
uv run pylint app
```

### Executar todos os verificadores

```bash
uv run pre-commit run --all-files
```

## 🔒 Segurança

### Análise de segurança com Bandit

```bash
uv run bandit -r app
```

### SAST com GitHub Actions

O workflow `security.yml` executa automaticamente:
- Bandit (vulnerabilidades em código Python)
- Dependency check (vulnerabilidades em dependências)
- CodeQL (análise de segurança avançada)

## 📚 Documentação

### MkDocs local

```bash
uv run mkdocs serve
```

Acesse em: http://localhost:8000

### Gerar documentação

```bash
uv run mkdocs build
```

## 🗄️ Database & Migrations

### Criar migração

```bash
uv run alembic revision --autogenerate -m "Descrição da migração"
```

### Aplicar migrations

```bash
uv run alembic upgrade head
```

### Reverter migração

```bash
uv run alembic downgrade -1
```

## 🔄 CI/CD Workflows

### 1. **CI Pipeline** (`.github/workflows/ci.yml`)

Executado em cada push/PR:
- Testes unitários
- Testes de integração
- Cobertura de código (mínimo 80%)
- Linting (Black, Ruff, mypy)
- Build do projeto

### 2. **Security Scan** (`.github/workflows/security.yml`)

Executado diariamente:
- Bandit (análise de segurança)
- Dependency check
- CodeQL analysis

### 3. **Deploy** (`.github/workflows/deploy.yml`)

Manual ou automático na main:
- Build da imagem Docker
- Push para registry
- Deploy em staging/production

## 🛠️ Configuração Git Hooks

Pre-commit hooks garantem qualidade antes de cada commit:

```bash
uv run pre-commit install
```

Os hooks irão:
- Verificar tamanho de arquivos
- Formatação com Black
- Linting com Ruff
- Type checking com mypy
- Verificações de YAML/JSON

## 📝 Variáveis de Ambiente

Copie `.env.example` para `.env` e configure:

```env
# Aplicação
APP_NAME=fastapi-complete-workflow
APP_ENV=development
DEBUG=True

# Banco de Dados
DATABASE_URL=postgresql://user:password@localhost:5432/apidb

# JWT
SECRET_KEY=seu-secret-key-muito-seguro
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8000

# Logging
LOG_LEVEL=INFO
```

## 🐳 Docker (Opcional)

```bash
# Build
docker build -t fastapi-api:latest .

# Run
docker run -p 8000:8000 --env-file .env fastapi-api:latest
```

## 📊 Métricas de Qualidade

- **Cobertura de Testes:** 80%+
- **Complexidade Ciclomática:** < 10
- **Tipo Checking:** Strict
- **Segurança:** Zero vulnerabilidades conhecidas

## 🤖 Fluxo de Desenvolvimento para IA

Para um agente de IA implementar features:

1. **Criar branch:**
   ```bash
   git checkout -b feat/nova-feature
   ```

2. **Desenvolver feature:**
   - Criar modelos em `app/models/`
   - Implementar serviços em `app/services/`
   - Criar endpoints em `app/api/v1/endpoints/`
   - Escrever schemas em `app/api/v1/schemas.py`

3. **Adicionar testes:**
   - Unit tests em `tests/unit/`
   - Integration tests em `tests/integration/`

4. **Validar qualidade:**
   ```bash
   uv run pre-commit run --all-files
   uv run pytest --cov=app
   uv run bandit -r app
   ```

5. **Commit e Push:**
   ```bash
   git add .
   git commit -m "feat: descrição da feature"
   git push origin feat/nova-feature
   ```

6. **PR automático:** CI/CD valida automaticamente

## 📖 Documentação Adicional

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [pytest](https://docs.pytest.org/)

## 📄 Licença

MIT - veja LICENSE para detalhes

## 👤 Autor

cerossi

---

**Desenvolvido com ❤️ para desenvolvimento de APIs profissionais**
