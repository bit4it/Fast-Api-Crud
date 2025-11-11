# FastAPI CRUD Application

A professional RESTful API built with FastAPI, PostgreSQL, and SQLAlchemy, featuring complete CRUD operations with authentication, database migrations, and comprehensive error handling.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Migrations](#database-migrations)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Testing](#testing)
- [Contributing](#contributing)

## ✨ Features

- ✅ Full CRUD operations for Items
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ API Key authentication via custom decorators
- ✅ Database migrations with Alembic
- ✅ Pydantic schemas for data validation
- ✅ Query filtering and pagination support
- ✅ Comprehensive error handling
- ✅ RESTful API design patterns
- ✅ Environment-based configuration
- ✅ Transaction management

## 📁 Project Structure

```
Fast-Api-Proj/
│
├── alembic/                      # Database migration files
│   ├── versions/                 # Migration versions
│   ├── env.py                    # Alembic environment configuration
│   ├── script.py.mako            # Migration template
│   └── README                    # Alembic documentation
│
├── app/                          # Main application package
│   ├── __init__.py
│   ├── main.py                   # FastAPI application entrypoint
│   │
│   ├── api/                      # API layer
│   │   ├── decorators.py         # Custom decorators (API key auth)
│   │   ├── item_resource.py     # Item endpoint handlers
│   │   └── routes.py             # API router configuration
│   │
│   ├── core/                     # Core configurations
│   │   ├── __init__.py
│   │   └── config.py             # Settings and environment variables
│   │
│   ├── db/                       # Database layer
│   │   └── connections.py        # Database connection and session
│   │
│   ├── models/                   # SQLAlchemy models
│   │   ├── base.py               # Base model with common fields
│   │   ├── item_models.py        # Item database model
│   │
│   ├── schemas/                  # Pydantic schemas
│   │   ├── item_schema.py        # Item request/response schemas
│   │
│   └── services/                 # Business logic layer
│       └── item_service.py       # Item CRUD operations
│
├── tests/                        # Test suite
│   ├── __init__.py
│   └── test_integration.py       # Integration tests
│
├── .env                          # Environment variables (not in git)
├── .gitignore                    # Git ignore rules
├── alembic.ini                   # Alembic configuration
└── README.md                     # Project documentation
```

## 🛠 Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- **Database:** PostgreSQL - Robust relational database
- **ORM:** SQLAlchemy - SQL toolkit and ORM
- **Migrations:** Alembic - Database migration tool
- **Validation:** Pydantic v2 - Data validation using Python type hints
- **Authentication:** Custom API Key decorator
- **Python Version:** 3.8+

## 📦 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Virtual environment tool (venv/virtualenv)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Fast-Api-Proj
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # .venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Create a `.env` file in the project root:**
   ```env
   # Database Configuration
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_NAME=your_db_name

   # API Security
   API_KEY=your_secret_api_key
   ```

2. **Update database credentials** in the `.env` file with your PostgreSQL details.

## 🗄️ Database Migrations

1. **Initialize Alembic (if not already done):**
   ```bash
   alembic init alembic
   ```

2. **Create a new migration:**
   ```bash
   alembic revision --autogenerate -m "description of changes"
   ```

3. **Apply migrations:**
   ```bash
   alembic upgrade head
   ```

4. **Rollback migration:**
   ```bash
   alembic downgrade -1
   ```

## 🏃 Running the Application

1. **Development mode with auto-reload:**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Production mode:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

3. **Access the application:**
   - API: http://localhost:8000
   - Interactive API docs (Swagger): http://localhost:8000/docs
   - Alternative API docs (ReDoc): http://localhost:8000/redoc

## 📚 API Documentation

Once the application is running, visit:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

These provide interactive documentation with the ability to test endpoints directly.

## 🔌 API Endpoints

### Health Check
```
GET /
Response: {"ok": "200"}
```

### Items

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/items` | Get all items | ✅ |
| GET | `/api/items/{item_id}` | Get item by ID | ✅ |
| GET | `/api/items/filter?price_min=X&price_max=Y` | Filter items by price | ✅ |
| POST | `/api/items` | Create new item | ✅ |
| POST | `/api/items/create_v2` | Create item (transaction version) | ✅ |
| PUT | `/api/items/{item_id}` | Update entire item | ✅ |
| PATCH | `/api/items/{item_id}` | Partially update item | ✅ |
| DELETE | `/api/items/{item_id}` | Delete item | ✅ |

### Request/Response Examples

**Create Item (POST `/api/items`)**
```json
Request:
{
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1200
}

Response (201 Created):
{
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1200,
  "created_at": "2025-11-12T10:30:00",
  "updated_at": "2025-11-12T10:30:00"
}
```

**Get Items with Filter (GET `/api/items/filter?price_min=100&price_max=500`)**
```json
Response (200 OK):
[
  {
    "id": 1,
    "name": "Mouse",
    "description": "Wireless mouse",
    "price": 250,
    "created_at": "2025-11-12T10:30:00",
    "updated_at": "2025-11-12T10:30:00"
  }
]
```

## 🔐 Authentication

This API uses API Key authentication via the `x-api-key` header.

**Add the header to your requests:**
```bash
curl -H "x-api-key: your_secret_api_key" http://localhost:8000/api/items
```

**Response codes:**
- `401 Unauthorized` - Missing API key
- `403 Forbidden` - Invalid API key

## 🧪 Testing

Run tests using pytest:

```bash
# Install pytest if not already installed
pip install pytest pytest-asyncio httpx

# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_integration.py
```

## 📝 Development Guidelines

### Adding a New Model

1. Create model in `app/models/`
2. Create schema in `app/schemas/`
3. Create service in `app/services/`
4. Create resource/endpoint in `app/api/`
5. Generate and apply migration

### Code Style

- Follow PEP 8 guidelines
- Use type hints for better code clarity
- Document functions with docstrings
- Keep business logic in service layer

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Aftab**

## 🙏 Acknowledgments

- FastAPI documentation and community
- SQLAlchemy ORM
- Pydantic validation library

---

**Note:** Remember to keep your `.env` file secure and never commit it to version control.
