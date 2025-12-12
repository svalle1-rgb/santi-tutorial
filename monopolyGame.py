import random

def diceRoll():
    input = input("Roll the dice! Press any keys!")
    if input:
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)
        print(f"You rolled {dice_one} and {dice_two}, a total of {dice_one + dice_two}!")
        return dice_one + dice_two

class Player:
    def __init__(self, name): # Attributes for the player object
        self.name = name
        self.money = 1500
        self.position = 0 # Position must start at Go 
        self.in_jail = False
        self.turns_in_jail = 0
        self.properties = []

class Property:
    def __init__(self, name, price, rent, house_cost, colour):
        self.name = name
        self.price = price
        self.rent = rent
        self.house_cost = house_cost
        self.house_num = 0
        self.owner = None
        self.colour = colour

class Railroad(Property):
    def __init__(self, name, price, rent=25, house_cost=0, colour=None):
        super().__init__(name, price)

    def railroad_rent(self): # Rent must be calculated as it works differently
        if self.owner is None:
            return 0
        railroads_owned =  sum(isinstance(p, Railroad) for p in self.owner.properties)
        if railroads_owned == 0:
            return 25
        else:
            return 25 * (2**(railroads_owned - 1))

class Utility(Property):
    def __init__(self, name, price):
        super().__init__(name, price, rent=25, house_cost=0, colour=None)

    def utility_rent(self, dice_total):
        if self.owner is None:
            return 0
        utilities_owned = sum(isinstance(p, Utility) for p in self.owner.properties)
        multiplier = 4 if utilities_owned == 1 else 10
        return dice_total * multiplier

# Anything under this is functional code 

properties_list = [
    {"name": "Old Kent Road", "colour": "Brown", "price": 60, "rent": [2, 10, 30, 90, 160, 250], "house_cost": 50},
    {"name": "Whitechapel Road", "colour": "Brown", "price": 60, "rent": [4, 20, 60, 180, 320, 450], "house_cost": 50},

    {"name": "The Angel Islington", "colour": "Light Blue", "price": 100, "rent": [6, 30, 90, 270, 400, 550], "house_cost": 50},
    {"name": "Euston Road", "colour": "Light Blue", "price": 100, "rent": [6, 30, 90, 270, 400, 550], "house_cost": 50},
    {"name": "Pentonville Road", "colour": "Light Blue", "price": 120, "rent": [8, 40, 100, 300, 450, 600], "house_cost": 50},

    {"name": "Pall Mall", "colour": "Pink", "price": 140, "rent": [10, 50, 150, 450, 625, 750], "house_cost": 100},
    {"name": "Whitehall", "colour": "Pink", "price": 140, "rent": [10, 50, 150, 450, 625, 750], "house_cost": 100},
    {"name": "Northumberland Avenue", "colour": "Pink", "price": 160, "rent": [12, 60, 180, 500, 700, 900], "house_cost": 100},

    {"name": "Bow Street", "colour": "Orange", "price": 180, "rent": [14, 70, 200, 550, 750, 950], "house_cost": 100},
    {"name": "Marlborough Street", "colour": "Orange", "price": 180, "rent": [14, 70, 200, 550, 750, 950], "house_cost": 100},
    {"name": "Vine Street", "colour": "Orange", "price": 200, "rent": [16, 80, 220, 600, 800, 1000], "house_cost": 100},

    {"name": "Strand", "colour": "Red", "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "house_cost": 150},
    {"name": "Fleet Street", "colour": "Red", "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "house_cost": 150},
    {"name": "Trafalgar Square", "colour": "Red", "price": 240, "rent": [20, 100, 300, 750, 925, 1100], "house_cost": 150},

    {"name": "Leicester Square", "colour": "Yellow", "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "house_cost": 150},
    {"name": "Coventry Street", "colour": "Yellow", "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "house_cost": 150},
    {"name": "Piccadilly", "colour": "Yellow", "price": 280, "rent": [24, 120, 360, 850, 1025, 1200], "house_cost": 150},

    {"name": "Regent Street", "colour": "Green", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "house_cost": 200},
    {"name": "Oxford Street", "colour": "Green", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "house_cost": 200},
    {"name": "Bond Street", "colour": "Green", "price": 320, "rent": [28, 150, 450, 1000, 1200, 1400], "house_cost": 200},

    {"name": "Park Lane", "colour": "Dark Blue", "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500], "house_cost": 200},
    {"name": "Mayfair", "colour": "Dark Blue", "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000], "house_cost": 200}
]
for property in properties_list:
    properties_list = []
    properties_list.append(Property(name=properties_list["name"], price=properties_list["price"], rent=properties_list["rent"], house_cost=properties_list["house_cost"], colour=properties_list["colour"]))
    

utilities_list = [
    {"name": "Electric Company", "price": 150},
    {"name": "Water Works", "price": 150}
]

railroads_list = [
    {"name": "King's Cross Station", "price": 200},
    {"name": "Marylebone Station", "price": 200},
    {"name": "Fenchurch St Station", "price": 200},
    {"name": "Liverpool St Station", "price": 200}
]

