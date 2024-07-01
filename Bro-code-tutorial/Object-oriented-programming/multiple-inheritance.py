# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass

class Lion(Predator):
    pass

class Fish(Predator, Prey): # Multiple inheritance
    pass

rabbit = Rabbit()
lion = Lion()
fish = Fish()

rabbit.flee()
lion.hunt()
fish.hunt()
fish.flee()