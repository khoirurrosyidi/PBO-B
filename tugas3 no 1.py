class User:
    def __init__(self, first,):
        self.firstname = first
    def PrintFirst(self):
        return self.firstname
class Programer(User):
    def __init__(self,  first, last):
        self.last = last
        User.__init__(self, first)
    def PrintLast (self):
        return self.last
    def Name(self):
        return self.firstname + " " + self.last
y = Programer("Brian","Diana")
print("NAMA DEPAN    : "+y.PrintFirst())
print("NAMA BELAKANG : "+y.PrintLast())
print("NAMA LENGKAP  : "+y.Name())
