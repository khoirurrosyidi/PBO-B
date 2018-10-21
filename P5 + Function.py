class Shark():
    def swim(self):
        print ("The Shark is swimming.")
    def swim_backwards(self):
        print ("The Shark cannot swim backwards, but can sink backwards.")
    def skeleton(self):
        print ("The Shark skeleton is made of cartilage.")

class Clownfish():
    def swim(self):
        print ("The Clownfish is swimming.")
    def swim_backwards(self):
        print ("The Clownfish can swim backwards.")
    def skeleton(self):
        print ("The Clownfish's skeleton is made of bone.")

def in_the_pacific(fish):
    fish.swim()
    
a = Shark()
b=Clownfish()

in_the_pacific(a)
in_the_pacific(b)
