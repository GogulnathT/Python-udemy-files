# objects are instances of classes 
# classes function as a blue print for objects defining their attributes and methods
# these objects have attributes and methods(actions)
# classes are usually written in a separate module and then imported (since they tend to be huge)

class Car: # name starts with capital

    # the init method is the constructor in python, used to create(initialize) objects
    def __init__(self,make,model,year,color): # these are arguments that will be assigned as attributes to the obj
        # these are attributes
        self.make = make # these are also known as instance variable 
        self.model = model
        self.year = year
        self.color = color
        # self represents the object that is using this class,
        # the attributes that are passed when an object is created can be assigned to that object
        # using the self.

    wheels = 4 # this is a class variable with default value as 4

    # these are methods
    def drive(self): 
        print("This", self.model ,"is driving")
        # calling an attribute of the object to be used by this method

    def stop(self):
        print("This", self.model ,"is stopping")


car1 = Car("Ford","Mustang",2014, "Blue")
car2 = Car("Toyota","Camry",2012,"Silver")

print(car1.model)
print(car2.make)
car1.drive()
car2.drive()

print(Car.wheels)
Car.wheels = 6 # here the class variable of class Car is changed for all the objects of this class 