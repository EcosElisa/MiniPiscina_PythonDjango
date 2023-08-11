import sys

def findStates():
    if(len(sys.argv) != 2):
        sys.exit(1)
        
    city = sys.argv[1]
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    if city in states:
        findCapital(states[city])
    else:
        print("Unknown state")

def findCapital(city):
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if capital_cities.get(city) == None:
        print("Unknown state")
    else:
        print(capital_cities[city])

if __name__ == '__main__':
    findStates()