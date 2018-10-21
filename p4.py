class Fish:
    def __init__(self, first_name, last_name="Fish", skelaton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skelaton = skelaton
        self.eyelids = eyelids
    def swim(self):
        print ("The Fish is Swimming.")
    def swim_backards(self):
        print("The Fish can swim backwards.")
class shark(Fish):
    def __init__(self,first_name,last_name="Shark",skelaton="cartilage",eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skelaton = skelaton
        self.eyelids = eyelids
    def swim_backwards(self):
        print("The Shark cannot swim backwards, but can sink backwards.")


hiu = shark("hiu besar")
hiu.swim_backwards()
