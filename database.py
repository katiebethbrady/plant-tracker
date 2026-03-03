from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

def connect():
    connection = psycopg2.connect(
    host = host,
    database = database,
    user = user,
    password = password
    )
    return connection

def db_add_plant(connection, plant):
    cursor = connection.cursor()
    cursor.execute(
    "INSERT INTO plants (name, species, location, last_watered) VALUES (%s, %s, %s, %s)",
    (plant.name, plant.species, plant.location, plant.last_watered)
    )
    connection.commit()
    cursor.close()

def db_get_all_plants(connection):
    cursor = connection.cursor()
    cursor.execute(
            "SELECT * FROM plants"
    )
    results = cursor.fetchall()
    cursor.close()
    return results

def db_delete_plant_by_ID(connection, id):
    cursor = connection.cursor()
    cursor. execute(
    "DELETE FROM plants WHERE id = %s", (id,)
    )
    connection.commit()
    cursor.close()

def db_search_plant(connection, search_term):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM plants where name = %s OR species = %s", (search_term, search_term)
    )
    results = cursor.fetchall()
    cursor.close()
    return results