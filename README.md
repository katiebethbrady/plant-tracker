# 🌱 Plant Tracker
A Python application to track and manage your plants, backed by a PostgreSQL database.

## Purpose
This project was built to practice and demonstrate practical Python skills including object oriented programming, input validation, error handling, REST API design, and database integration. The app began as a CLI application and was refactored into a REST API using FastAPI.

## Project Structure
- `main.py` — original CLI application entry point and menu logic
- `plant.py` — Plant class definition
- `database.py` — database connection and queries
- `app.py` — FastAPI REST API endpoints

## Technologies
- Python 3
- FastAPI
- PostgreSQL
- psycopg2
- python-dotenv
- uvicorn

## API Endpoints
- `GET /plants` — retrieve all plants
- `POST /plants` — add a new plant
- `DELETE /plants/{id}` — delete a plant by id
- `GET /plants/search?term=` — search plants by name or species

## Setup
1. Clone the repository
2. Install dependencies:
```
pip install psycopg2-binary python-dotenv fastapi uvicorn
```
3. Create a `.env` file in the root directory with the following:
```
DB_HOST=localhost
DB_NAME=plant_tracker
DB_USER=postgres
DB_PASSWORD=yourpassword
```
4. Set up PostgreSQL and create the `plants` table:
```sql
CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    location TEXT NOT NULL,
    last_watered TEXT NOT NULL
);
```
5. Run the API:
```
uvicorn app:app --reload
```
6. View interactive API docs at:
```
http://127.0.0.1:8000/docs
```

## Features
- Add, view, search, and delete plants
- REST API with auto-generated Swagger documentation
- Object oriented design using a Plant class
- Input validation with user friendly error messages
- Data persists to a PostgreSQL database
- Evolved from a CLI app to a full REST API