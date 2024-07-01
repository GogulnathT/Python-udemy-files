# multi-level inheritance = a child class(derived) also inherits from another child(derived) class 

class Organism:
    alive = True

class Animal(Organism):
    
    def eat(self):
        print("Animal eats")
    
class Dog(Animal): # Dog is derived from Animal(which is derived from Organism)
    def bark(self):
        print('dog barks')

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()