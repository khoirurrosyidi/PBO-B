class User:
    name=""
    def __init__ (self,name):
        self.name = name

    def printName(self):
        print ("Name=" + self.name)

class Programer(User):
    def __init__(self,name):
        self.name = name
    def doPython(self):
        print ("programming Python")

Irul = User ("IRUL")
Irul.printName()
Lulus = Programer("LULUS")
Lulus.printName()
Lulus.doPython()

