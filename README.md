# Room API - CRUD REST Completo

Sistema de reservas de salas de conferencias para una empresa.

## Stack Tecnológico

- **Framework**: FastAPI 0.104+
- **ORM**: SQLAlchemy 2.0+ con Alembic
- **Base de datos**: PostgreSQL
- **Python**: 3.10+
- **Testing**: pytest con pytest-asyncio

## Instalación

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql://user:password@localhost/room_api
PYTHON_ENV=development
LOG_LEVEL=INFO
```

## Ejecución

```bash
uvicorn src.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Tests

```bash
pytest tests/ -v --cov=src
```

## Documentación

Documentación interactiva: `http://localhost:8000/docs`
