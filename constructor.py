class person:
    def __init__(self,name,occ):
        print("Hey i am constructor")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")
a= person("Rohit", "Data analyst")
a.info()