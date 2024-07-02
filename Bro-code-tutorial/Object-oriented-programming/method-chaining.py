# method chaining = calling multiple methods sequentially 
#                   each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("Car turns on")
        return self # adding this is to use method chaining 
    
    def drive(self):
        print("Car drives")
        return self
    
    def brake(self):
        print("Car brakes")
        return self
    
    def turn_off(self):
        print("Car turns off")
        return self

car = Car()

car.turn_on().drive().brake().turn_off() # method chaining; since self is returned the next method is executed