import sys

def find_place():
    if(len(sys.argv) < 2):
        return
    if(len(sys.argv) < 2):
        return
    
    result = ""
    list =  sys.argv[1]
    expressions = list.split(',')
    for value in expressions:
        if(len(value) <= 1):
            continue
        
        val = value.strip()
        val = val.title()
        result = city_per_capital(val)
        if result is None: 
            result = capital_per_city(val)
            if result is None: 
                print(val, "is neither a capital city nor a state")


def capital_per_city(place):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    
    if place in states:
        return findCapital(states[place], place)
    
def findCapital(city, original):
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if capital_cities.get(city) != None:
       print(original, "is the state of", capital_cities[city])
       return capital_cities[city]
      
def city_per_capital(place):
    capital = place
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if capital in capital_cities.values():
        for key, value in capital_cities.items():
            if capital == value:
                return findCity(key, capital)

def findCity(capital, original):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    
    if capital in states.values():
        for key, value in states.items():
            if capital == value:
                print(original, "is the capital of", key)
                return key
  
    
if __name__ == '__main__':
    find_place()