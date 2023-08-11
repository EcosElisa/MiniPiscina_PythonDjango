import sys

def capital_per_city(args):
    capital = sys.argv[1]
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if capital in capital_cities.values():
        for key, value in capital_cities.items():
            if capital == value:
                findCity(key)
    else:
        print("Unknown capital city")

def findCity(capital):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    
    if capital in states.values():
        for key, value in states.items():
            if capital == value:
                print(key)
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        sys.exit(1)
    capital_per_city(sys.argv)
