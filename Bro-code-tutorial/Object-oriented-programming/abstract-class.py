# An abstract class can be considered a blueprint for other classes. 
# It allows you to create a set of methods that must be created within
# any child classes built from the abstract class.

# abstract class = a class which contains one or more abstract methods 
# atleast one abstract class is needed to make the class Abstract
# child classes which inherit from abstract classes must have an implementation of the abstract method
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod
# abc = abstract base class module; 

class Vehicle(ABC):
    @abstractmethod # this makes Vehicle an abstract class; so Vehicle object cannot be created
    def go(self):
        pass

    def stop(self):
        print("stops")

class Car(Vehicle):
    def go(self):
        print("Car goes")

class Bike(Vehicle):
    def go(self):
        print("Bike goes")

# car1 = Vehicle() # this will cause an error as Vehicle()is an abstract class
car1 = Car()
car1.go()
car1.stop()
