🌱 Plant Tracker
    A command-line application built with Python to track and manage your plants.

Purpose
    This project was built to practice and demonstrate fundamental Python concepts including object oriented programming, input validation, error handling, and clean code structure.

Project Structure
    main.py — application entry point and menu logic
    plant.py — Plant class definition

Technologies 
    Python 3
    PostgreSQL
    psycopg2
    python-dotenv

Setup
    1. Clone repository
    2. Install dependencies: 
        pip install psycopg2-binary python-dotenv
    3. Create .env file in the root directory with the following:
        DB_HOST=localhost
        DB_NAME=plant_tracker
        DB_USER=postgres
        DB_PASSWORD=yourpassword
    4. Setup PostgreSQL and create the plants table
        CREATE TABLE plants (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            location TEXT NOT NULL,
            last_watered TEXT NOT NULL
        );

    5. Run the app:
        python main.py

Features
    Add a plant with name, species, location, and last watered date
    View all plants
    Input validation with user friendly error messages
    Object oriented design using a Plant class
    Data persists to a PostgreSQL database