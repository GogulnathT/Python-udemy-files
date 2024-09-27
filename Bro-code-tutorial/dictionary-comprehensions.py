# dict comprehensions = create dictionaries using an expression
#                       can replace for loops and certain lambda functions
#
# dictionary = {key: expression for key/value in iterable}
# dictionary = {key: expression for key/value in iterable if conditional}
# dictionary = {key: (if/else) for key/value in iterable}
# dictionary = {key: function(value) for key/value in iterable}

# eg1 for first case
cities_in_Far = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_Cel = {key: round((value - 32)*(5/9)) for (key, value) in cities_in_Far.items()}
print(cities_in_Cel)

# eg2
weather = {'New York': 'snowy', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_weather = {key: value for (key,value) in weather.items() if value == 'sunny'}
print((sunny_weather))

# eg3
cities_in_Far = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
weather_cities = {key: 'warm' if value >=60 else 'cold' for(key,value) in cities_in_Far.items()}
print(weather_cities)

# eg4
def check_temp(value):
    if value >= 70:
        return 'hot'
    elif value >= 40:
        return 'mild'
    else: return 'freezing'

cities_in_Far = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for(key,value) in cities_in_Far.items()}
print(desc_cities)


