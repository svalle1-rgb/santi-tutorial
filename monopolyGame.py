import random

class Player:
    def __init__(self, name): # Attributes for the player object
        self.name = name
        self.money = 1500
        self.position = 0 # Position must start at Go 
        self.in_jail = False
        self.turns_in_jail = 0
        self.properties = []
        self.bankruptcy = False
        self.escape_jail = False

class Bank:
    def __init__(self):
        self.money = 100000000000000000000000
    def transaction(self, sender, amount, receiver=None):
        sender.money -= amount
        if receiver is not None:
            receiver.money += amount
        if sender.money < 0:
            sender.bankruptcy = True


class Tile:
    def __init__(self, name): # Highest class in the inheritance hirearchy, non ownable tiles can inherit from this
        self.name = name
    
    def landed_on(self, player):
        pass

class Tile_Ownable(Tile):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price
        self.owner = None
    
    def landed_on(self, player):
        print(f"{player.name} has landed on {self.name}")
        
        if self.owner is None:
            if player.money < self.price:
                print(f"{player.name} cannot afford {self.name}.")
                return
            
            buy = input(f"{self.name} is unowned. Buy for {self.price}? (y/n): ")
            if buy.lower() == "y":
                Bank.transaction(player, self.price)
                self.owner = player
                player.properties.append(self)
                print(f"{player.name} has bought {self.name}!")


class Property(Tile_Ownable): # Property, automatically inerhits owner and isn't needed to call it again
    def __init__(self, name, price, rent, house_cost, colour):
        super().__init__(name, price)
        self.rent = rent
        self.house_cost = house_cost
        self.colour = colour
        self.house_number = 0

    def landed_on(self, player):
        super().landed_on(player)
        if self.owner is not None and self.owner != player:
            print(f"{player.name} has landed on the property of {self.owner.name}, therefore must pay them ${self.rent[self.house_number]}")
            Bank.transaction(player, self.rent[self.house_number], self.owner)

class Railroad(Tile_Ownable): # No need for a __init__ function since it inherits everything it needs
    def railroad_rent(self): # Rent must be calculated relative to how many railroads owned
        if self.owner is None:
            return 0
        railroads_owned = sum(isinstance(p, Railroad) for p in self.owner.properties)
        return 25 * (2**(railroads_owned - 1))
    
    
    def landed_on(self, player):
        super().landed_on(player)
        rent = self.railroad_rent()
        railroads_owned = sum(isinstance(p, Railroad) for p in self.owner.properties)
        if self.owner is not None and self.owner != player:
            print(f"{player.name} must pay rent of ${rent} to {self.owner.name}, who owns {railroads_owned} railroad(s) (1=25,2=50,3=100,4=200)")
            Bank.transaction(player, rent, self.owner)

class Utility(Tile_Ownable):
    def utility_rent(self, dice_total):
        if self.owner is None:
            return 0
        utilities_owned = sum(isinstance(p, Utility) for p in self.owner.properties)
        multiplier = 4 if utilities_owned == 1 else 10
        return dice_total * multiplier
    
    def landed_on(self, player, dice_total):
        super().landed_on(player)
        rent = self.utility_rent(dice_total)
        utilities_owned = sum(isinstance(p, Utility) for p in self.owner.properties)
        if self.owner is not None and self.owner != player:
            print(f"{player.name} must pay rent of ${rent} to {self.owner.name}, who owns {utilities_owned} utility(ies) (Rent = {dice_total} * {rent / dice_total})")

class Chance(Tile):
    def __init__(self):
        super().__init__("Chance")
    def landed_on(self, player):
        pass

class Community(Tile):
    def __init__(self):
        super().__init__("Community Chest")
    def landed_on(self, player):
        pass

class Go(Tile):
    def __init__(self):
        super().__init__("Go")
    def landed_on(self, player):
        pass

class Jail(Tile):
    def __init__(self):
        super().__init__("Jail")
    def landed_on(self, player):
        pass

class Go_Jail(Tile):
    def __init__(self):
        super().__init__("Go to jail")
    def landed_on(self, player):
        pass

class Parking(Tile):
    def __init__(self):
        super().__init__("Free Parking")
    def landed_on(self, player):
        pass

class Tax(Tile):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

    def landed_on(self, player):
        pass

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
properties_objects = []
for prop in properties_list:
    properties_objects.append(Property(name=prop["name"], colour=prop["colour"], price=prop["price"], rent=prop["rent"], house_cost=prop["house_cost"]))

utilities_list = [
    {"name": "Electric Company", "price": 150},
    {"name": "Water Works", "price": 150}
]
utilities_objects = []
for util in utilities_list:
    utilities_objects.append(Utility(name=util["name"], price=util["price"]))

railroads_list = [
    {"name": "King's Cross Station", "price": 200},
    {"name": "Marylebone Station", "price": 200},
    {"name": "Fenchurch St Station", "price": 200},
    {"name": "Liverpool St Station", "price": 200}
]
railroads_objects = []
for rr in railroads_list:
    railroads_objects.append(Railroad(name=rr["name"], price=rr["price"]))

board = [
    Go(),
    properties_objects[0],
    Community(),
    properties_objects[1],
    Tax(name="Income Tax", amount=200),
    railroads_objects[0],
    properties_objects[2],
    Chance(),
    properties_objects[3],
    properties_objects[4],
    Jail(),
    properties_objects[5],
    utilities_objects[0],
    properties_objects[6],
    properties_objects[7],
    railroads_objects[1],
    properties_objects[8],
    Community(),
    properties_objects[9],
    properties_objects[10],
    Parking(),
    properties_objects[11],
    Chance(),
    properties_objects[12],
    properties_objects[13],
    railroads_objects[2],
    properties_objects[14],
    properties_objects[15],
    utilities_objects[1],
    properties_objects[16],
    Go_Jail(),
    properties_objects[17],
    properties_objects[18],
    Community(),
    properties_objects[19],
    railroads_objects[3],
    Chance(),
    properties_objects[20],
    Tax(name="Super Tax", amount=100),
    properties_objects[21]
]

def dice_roll(player):
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    print(f"{player.name} rolled {die_one} and {die_two}! A total of {die_one + die_two}")
    return [die_one, die_two, (die_one + die_two)]

def turn(player, board):
    dice_total = dice_roll(player)
    if isinstance(board[player.position], Utility):
        board[player.position].landed_on(player, dice_total)
    else:
        board[player.position].landed_on(player)


def move_player(p, total=None, target_index=None, collect_go=False):
    old_position = p.position
    if target_index is None:
        p.position = (p.position + total) % len(board)
        if p.position < old_position:
            print(f"{p.name} has passed Go! Collect $200")
            p.money += 200
        current_tile = board[p.position]
        if isinstance(current_tile, Utility):
            current_tile.landed_on(p, total or 0)
        else:
            current_tile.landed_on(p)
    else:
        p.position = target_index % len(board)
        if collect_go and p.position < old_position:
                print(f"{p.name} has passed Go! Collect $200")
                p.money += 200

        current_tile = board[p.position]
        if isinstance(current_tile, Utility):
            current_tile.landed_on(p, total)
        else:
            current_tile.landed_on(p)
    
utility_indexes = [12, 28]

def nearest_utility(position):
    for idx in utility_indexes:
        if idx > position:
            return idx
    return utility_indexes[0]

rr_indexes = [5, 15, 25, 35]

def nearest_rr(position):
    for idx in rr_indexes:
        if idx > position:
            return idx
    return rr_indexes[0]    
    

def main():
    player_num = int(input("How many players are there? "))
    players = []
    for x in range(player_num):
        name = input(f"What is the name of player {x + 1}? ")
        players.append(Player(name))
    
    while True:
        for p in players:
            die1, die2, total = dice_roll(p)
            print(f"{p.name} has rolled {die1} and {die2}!")
            move_player(p, total)
