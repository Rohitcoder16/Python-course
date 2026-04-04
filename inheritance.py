class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id

    def showdetails(self):
            print(f"the name of employee {self.name}  ID is {self.id}")

class programmer(Employee):
    def showlanguage(self):
        print("the language is python")

e1=Employee("Rohit", 16)
e1.showdetails()
p1=programmer("Harry bhai", 17)
p1.showdetails()
p1.showlanguage()