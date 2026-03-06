from fastapi import FastAPI
from pydantic import BaseModel
from plant import Plant
from database import connect, db_get_all_plants, db_add_plant, db_delete_plant_by_ID, db_search_plant, db_update_last_watered

class PlantRequest(BaseModel):
    name: str
    species: str
    location: str
    last_watered: str

class WateringUpdate(BaseModel):
    last_watered: str

app = FastAPI()

@app.get("/plants")
def get_all_plants():
    connection = connect()
    all_plants = db_get_all_plants(connection)
    return all_plants

@app.post("/plants")
def add_plant(request: PlantRequest):
    connection  = connect()
    new_plant = Plant(request.name, request.species, request.location, request.last_watered) 
    db_add_plant(connection, new_plant)
    return {"message": f"{request.name} added successfully!"}

@app.delete("/plants/{id}")
def delete_plant(id: int):
    connection = connect()
    db_delete_plant_by_ID(connection, id)
    return {"message": f"Plant {id} deleted successfully!"}

@app.get("/plants/search")
def search_plant(term: str):
    connection = connect()
    results = db_search_plant(connection, term)
    return results

@app.put("/plants/{id}")
def update_last_watered(id: int, request: WateringUpdate):
    connection = connect()
    db_update_last_watered(connection, id, request.last_watered)
    return {"message": f"Plant {id} updated successfully!"}

