class Plant:
    def __init__(self, name, species, location, last_watered):
        self.name = name
        self.species = species
        self.location = location
        self.last_watered = last_watered

    def display(self):
        print(f"{self.name}")
        print(f"{self.species}")
        print(f"{self.location}")
        print(f"{self.last_watered}")