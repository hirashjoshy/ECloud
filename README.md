# User Management API

This project provides a REST API for user management using FastAPI, SQLAlchemy, and CockroachDB. The API supports basic CRUD operations, including creating, retrieving, updating, and deleting users.

## Project Structure

- `database.py`: Contains the database connection logic.
- `models.py`: Defines Pydantic models for data validation.
- `routes.py`: Implements API endpoints for user management.
- `schemas.py`: Defines the SQLAlchemy ORM models and database schema.