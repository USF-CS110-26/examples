class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return  self.name

    def get_species(self):
        return   self.species

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def play(self):
        print(f"{self.name} is playing.")


my_pet = Pet("Goldie", "cat")
print(my_pet)
