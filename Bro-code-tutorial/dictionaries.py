#dictionaries = Mutable, unordered collection of unique key value pairs 
#               Fast because they use hashing, allows quick access of a value 

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "France":"Paris",
            "UK":"London"}

print(capitals)
print(capitals.get("India"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.update({"Germany":"Berlin"}) #can be used to update existing values of key value pairs or add new
print(capitals.items())

capitals.pop('Germany')
