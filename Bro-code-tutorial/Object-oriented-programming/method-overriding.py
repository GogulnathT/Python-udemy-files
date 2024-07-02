# Method overriding is an ability of any object-oriented programming language that allows 
# a subclass or child class to provide a specific implementation of a method that is already provided 
# by one of its super-classes or parent classes.
# Method overriding is done by defining the same function signature method in the child class as that of 
# the parent class 

class Animal:
    def eat(self):
        print("Animal eats")

class Rabbit(Animal):
    def eat(self): # method with same function signature(name and args) as parent class 
        print("Rabbit eats")
    
    
ani = Animal()
rabbit = Rabbit()

ani.eat()
rabbit.eat() # used the method defined in this class instead of the parent class 
