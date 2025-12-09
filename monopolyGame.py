import csv
import random

class Space:
    def __init__(self, name, position):
        self.name = name
        self.position = position


    def landOn(self, player):
        pass

class Go(Space):
    def __init__(self, name):
        self.name = name
    
    def landOn(self, player):
        player.wallet += 200




class Property(Space):
    def __init__(self, name, position, price, rent, colour, houses, hotel, properties, owner=None, isOwned=False):
        super.__init__(name, position)
        self.price = price
        self.rent = rent
        self.colour = colour
        self.owner = ""

    def getRent(rent, houses, hotel):
        return (rent * (1 + 0.5 * houses) + (hotel * 2 * rent))

    def landOn(self, player, owner):
        if owner==None:
            buy = input("Would you like to buy {name} for {price}? (y/n)")
            if buy.lower() == "y":
                transaction(player, price)
                owner = player
            else:
                pass
        else:
            transaction(player, owner, getRent(rent, houses, hotel))

class CommunityChest(Space):
    def __init__(self, position):
        pass
                
            

class Player:
    def __init__(self, name, position, wallet=1500, bankruptcy=False, properties=[]):
        self.name = name
        self.position = position
        self.wallet = wallet
        self.bankruptcy = bankruptcy
        self.properties = properties


class Bank:
    def transaction(self, sender, amount, receiver=None):
        sender.money -= amount
        if receiver:
            receiver.money += amount
    
    def bankruptcyCheck(self, player):
        if player.wallet <= 0:
            player.bankruptcy = True

def toInt(value):
    return int(value) if value else 0

properties = [
{"name": "Go"}, # 0
{"name": "Old Kent Road", "colour": "Brown", "price": 60, "rent": [2,10,30,90,160,250], "houseCost": 50, "rentType": "property"}, # 1
{"name": "Community Chest"}, # 2
{"name": "Whitechapel Road", "colour": "Brown", "price": 60, "rent": [4,20,60,180,320,450], "houseCost": 50, "rentType": "property"}, # 3
{"name": "Income Tax"}, # 4
{"name": "King's Cross Station", "colour": "", "price": 200, "rent": [25,50,100,200], "houseCost": "", "rentType": "railroad"}, # 5
{"name": "The Angel Islington", "colour": "Light-Blue", "price": 100, "rent": [6,30,90,270,400,550], "houseCost": 50, "rentType": "property"}, # 6
{"name": "Chance"}, # 7
{"name": "Euston Road", "colour": "Light-Blue", "price": 100, "rent": [6,30,90,270,400,550], "houseCost": 50, "rentType": "property"}, # 8
{"name": "Pentonville Road", "colour": "Light-Blue", "price": 120, "rent": [8,40,100,300,450,600], "houseCost": 50, "rentType": "property"}, # 9
{"name": "Jail / Just Visiting"}, # 10
{"name": "Pall Mall", "colour": "Pink", "price": 140, "rent": [10,50,150,450,625,750], "houseCost": 100, "rentType": "property"}, # 11
{"name": "Electric Company", "colour": "", "price": 150, "rent": [0,0,0,0,0,0], "houseCost": "", "rentType": "utility"}, # 12
{"name": "Whitehall", "colour": "Pink", "price": 140, "rent": [10,50,150,450,625,750], "houseCost": 100, "rentType": "property"}, # 13
{"name": "Northumberland Avenue", "colour": "Pink", "price": 160, "rent": [12,60,180,500,700,900], "houseCost": 100, "rentType": "property"}, # 14
{"name": "Marylebone Station", "colour": "", "price": 200, "rent": [25,50,100,200], "houseCost": "", "rentType": "railroad"}, # 15
{"name": "Bow Street", "colour": "Orange", "price": 180, "rent": [14,70,200,550,700,900], "houseCost": 150, "rentType": "property"}, # 16
{"name": "Community Chest"}, # 17
{"name": "Marlborough Street", "colour": "Orange", "price": 180, "rent": [14,70,200,550,700,900], "houseCost": 150, "rentType": "property"}, # 18
{"name": "Vine Street", "colour": "Orange", "price": 200, "rent": [16,80,220,600,800,1000], "houseCost": 150, "rentType": "property"}, # 19
{"name": "Free Parking"}, # 20
{"name": "Strand", "colour": "Red", "price": 220, "rent": [18,90,250,700,875,1050], "houseCost": 150, "rentType": "property"}, # 21
{"name": "Chance"}, # 22
{"name": "Fleet Street", "colour": "Red", "price": 220, "rent": [18,90,250,700,875,1050], "houseCost": 150, "rentType": "property"}, # 23
{"name": "Trafalgar Square", "colour": "Red", "price": 240, "rent": [20,100,300,750,925,1100], "houseCost": 150, "rentType": "property"}, # 24
{"name": "Fenchurch St Station", "colour": "", "price": 200, "rent": [25,50,100,200], "houseCost": "", "rentType": "railroad"}, # 25
{"name": "Leicester Square", "colour": "Yellow", "price": 260, "rent": [22,110,330,800,975,1150], "houseCost": 150, "rentType": "property"}, # 26
{"name": "Coventry Street", "colour": "Yellow", "price": 260, "rent": [22,110,330,800,975,1150], "houseCost": 150, "rentType": "property"}, # 27
{"name": "Water Works", "colour": "", "price": 150, "rent": [0,0,0,0,0,0], "houseCost": "", "rentType": "utility"}, # 28
{"name": "Piccadilly", "colour": "Yellow", "price": 280, "rent": [24,120,360,850,1025,1200], "houseCost": 150, "rentType": "property"}, # 29
{"name": "Go to Jail"}, # 30
{"name": "Regent Street", "colour": "Green", "price": 300, "rent": [26,130,390,900,1100,1275], "houseCost": 200, "rentType": "property"}, # 31
{"name": "Oxford Street", "colour": "Green", "price": 300, "rent": [26,130,390,900,1100,1275], "houseCost": 200, "rentType": "property"}, # 32
{"name": "Community Chest"}, # 33
{"name": "Bond Street", "colour": "Green", "price": 320, "rent": [28,150,450,1000,1200,1400], "houseCost": 200, "rentType": "property"}, # 34
{"name": "Liverpool Street Station", "colour": "", "price": 200, "rent": [25,50,100,200], "houseCost": "", "rentType": "railroad"}, # 35
{"name": "Chance"}, # 36
{"name": "Park Lane", "colour": "Dark-Blue", "price": 350, "rent": [35,175,500,1100,1300,1500], "houseCost": 200, "rentType": "property"}, # 37
{"name": "Super Tax"}, # 38
{"name": "Mayfair", "colour": "Dark-Blue", "price": 400, "rent": [50,200,600,1400,1700,2000], "houseCost": 200, "rentType": "property"} # 39
]

for item in properties:
