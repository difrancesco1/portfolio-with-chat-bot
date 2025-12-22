# Getting Started (Backend)

This project uses:
- FastAPI
- PostgreSQL
- Docker & Docker Compose
- SQLAlchemy (async)
- Alembic migrations

---

## Prerequisites

Install the following:

- Python **3.10.12**
- Pip **25.3+**
- Docker & Docker Compose

Verify installs:

```bash
python3 --version        # should be 3.10.12
docker --version
```

## Python Virtual Environment

```bash
# Create virtual environment (run from project root or server/)
python3.10 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a virtual environment. This can be in the directories portfolio-with-chat-bot, or server.
python3.10 -m venv .venv

# Activate the virtual environment you just created
source .venv/bin/activate

# In the terminal, you should see (.venv) next to your cwd, or name
# Navigate to the server directory and install all dependencies in requirements
pip install -r requirements.txt
```

## Docker Compose commands:
```bash
# Build and start API + DB (detached)
docker compose up -d --build

# Stop containers and remove volumes (RESET DATABASE)
docker compose down -v

# Start API + DB (detached), for future starts after build
docker compose up -d
```

## Alembic Migrations
```bash
# Initialize Alembic (run ONCE)
docker compose exec api alembic init alembic

# Generate migration
docker compose exec api alembic revision --autogenerate -m "initial tables"

# Apply migration
docker compose exec api alembic upgrade head
```

## Database verification
```bash
# List database tables
docker compose exec db psql -U portfolio -d portfolio -c "\dt"
```

## API Verification
```bash
# Swagger UI
curl http://localhost:8000/docs
```