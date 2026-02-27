from plant import Plant                               # import Plant class
from database import connect, db_add_plant            # importing fnc for DB connection, fnc for add plant to table

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
    print("\t1. Add a plant")
    print("\t2. View all plants")
    print("\t3. Quit")

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
            if not plant_list:
                print("No plants added yet.")
            else:   
                for item in plant_list: 
                    item.display()

        elif choice == "3":
            break  
        else:
            print("Invalid option. Try again by entering an option 1-3.") 

main()
