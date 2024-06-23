import random

x = random.randint(1,232) #generates a random int within the given range
print('x: ',x) 

y = random.random() #generates a random float between 0 and 1
print("y-",y)

directions = ["north",'south','east','west']
print(random.choice(directions)) #choses a random choice from a sequence

nums = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(nums) #shuffles a collection 
print(nums) 