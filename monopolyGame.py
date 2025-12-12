class Player:
    def __init__(self, name): # Attributes for the player object
        self.name = name
        self.money = 1500
        self.position = 0 # Position must start at Go 
        self.in_jail = False
        self.turns_in_jail = 0
        self.properties = []

class Property:
    def __init__(self, name, price, rent, house_cost)
