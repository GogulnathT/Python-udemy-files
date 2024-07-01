# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called base class
# Child class is the class that inherits from another class, also called derived class
# Inheritance allows avoiding repetition of code; updating code becomes easier as it needs to be done once

class Animal:

    alive = True

    def eating(self):
        print("eating")
    
    def sleeping(self):
        print("sleeping")

class Rabbit(Animal): # Rabbit is inheriting all the attributes and methods of Animal
    def run(self): # method of rabbit that is not inherited
        print("rabbit runs")

class Fish(Animal):
    def swim(self):
        print("fish swims")

class Hawk(Animal):
    def fly(self):
        print("hawk flys")

rabbit = Rabbit()
fish = Fish()

print(rabbit.alive) # attribute of parent(Animal) in rabbit(Child) object
fish.sleeping()

fish.swim()