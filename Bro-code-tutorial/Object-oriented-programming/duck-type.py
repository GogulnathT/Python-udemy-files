# duck typing = concept where the class of an object is less important than the methods/attributes;
#               class type is not checked if minimum methods/attributes are present

class Duck:
    def walk(self):
        print("Duck is walking")
    
    def talk(self):
        print('Duck quacks')

class Chicken:
    def walk(self):
        print("Chicken is walking")
    
    def talk(self):
        print('Chicken clucks')
    
class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck) # here we are sending an duck object as it is a required parameter
person.catch(chicken) #we can send other object types as long as the object being sent has the same methods/attributes as that
                      #of expected ones i.e in this eg both chicken and duck have the same methods defined in their class