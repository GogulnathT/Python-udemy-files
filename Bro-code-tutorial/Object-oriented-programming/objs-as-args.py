class Car:
    colour = None

class Bike:
    colour = None

def change_color(x, colour):
    x.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1,"Blue")
change_color(car_2,"Red")
change_color(car_3,"White")

bike_1 = Bike()

change_color(bike_1,"Black")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(bike_1.colour)



