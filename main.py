from plant import Plant                 # import Plant class
from database import *                  # import all db functions


def add_plant():                        # new plant information

    while True:
        plant_name = input("Enter the name of your plant: ").strip()
        if plant_name:
            break
        else:
            print("Oops, try again! Enter a valid name!")
    while True:
        plant_species = input("Enter the species of your plant: ").strip()
        if plant_species:
            break
        else:
            print("Oops, try again! Enter a valid species!")
    while True:
        plant_location = input("Enter the location of the plant (indoor or outdoor): ").strip()
        if plant_location.lower() in ["indoor", "outdoor"]:
            break
        else:
            print("Oops, try again! Is your plant located indoor or outdoor?")
    while True:
        last_watered = input("Enter the last watered date (MM/DD/YYYY): ").strip()
        if last_watered:
            break
        else:
            print("Oops, try again! Enter a valid date.")

    new_plant = Plant(plant_name, plant_species, plant_location, last_watered)
    return new_plant

def menu():
    print("Menu:")
    print("\t1. Add a plant")
    print("\t2. View all plants")
    print("\t3. Delete a plant")
    print("\t4. Search for a plant")
    print("\t5. Quit")

def main():
    connection = connect()
    plant_list = []
    while True:
        menu()
        choice = input("Choose a menu option: ").strip()
        if choice == "1":
            new_plant = add_plant()
            plant_list.append(new_plant)
            db_add_plant(connection, new_plant)
        elif choice == "2":  
            rows = db_get_all_plants(connection)
            for row in rows:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Species: {row[2]}")
                print(f"Location: {row[3]}")
                print(f"Last Watered: {row[4]}\n")  
        elif choice == "3":
            id = input("Please enter an ID to delete plant: ").strip()
            db_delete_plant_by_ID(connection, id)
            print("Successfully deleted plant from database!")

        elif choice == "4":
            search_term = input("Search for name or species: ")
            search_results = db_search_plant(connection, search_term)
            for row in search_results:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Species: {row[2]}")
                print(f"Location: {row[3]}")
                print(f"Last Watered: {row[4]}\n")

        elif choice == "5":
            break  
        else:
            print("Invalid option. Try again by entering an option 1-3.") 

main()
