class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language
p1 = programmer("Rohit", 101, "Python")
print(p1.name)
print(p1.id)
print(p1.language)