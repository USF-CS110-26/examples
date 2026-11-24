class Pet:
	def __init__(self, name, species):
		self.name = name
		self.species  = species

	def get_name(self):
		return self.name

	def get_species(self):
		return self.species	

	def eat(self):
		print(f"{self.name} am eating!")

	def __str__(self):
		return self.name + ", " + self.species;	

my_cat = Pet("Goldie", "cat")
print(my_cat)


d  = Pet("Max", "dog")
print(d)


