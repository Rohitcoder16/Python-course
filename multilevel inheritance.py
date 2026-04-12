class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
class Dog(Animal):
    def __init__(self, name, species, breed):
        Animal.__init__(self, name , species= "Dog")
        print(f"Bread: {breed}")

class GoldenRetriver(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,  name, species= "Dog", breed= "GoldenRetriver")
        self.color = color
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

O = GoldenRetriver("Buddy", "Black")
O.show_details()