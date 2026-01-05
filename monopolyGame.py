from pizza import players, board, move_player, nearest_rr, nearest_utility

def Chance_Card:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
    
    def apply(self, player):
        self.effect(player, bank, players)

Chance_card("Adv_Go"):
    def advance_to_go(self, player, bank):
        print("Advance to Go!")
        move_player(player, target_index=0)

def go_to_jail(player, bank):
    print("Go to Jail. Move directly to Jail, do not pass Go or collect $200.")
    player.in_jail = True
    player.turns_in_jail = 0
    move_player(player, target_index=10)

def advance_to_pallmall(player, bank, players):
    print("Advance to Pall Mall! If you pass Go, collect $200!")
    move_player(player, target_index=11, collect_go=True)

def advance_to_trafalgar(player, bank, players):
    print("Advance to Trafalgar Square! If you pass Go, collect $200")
    move_player(player, target_index=24, collect_go=True)

def advance_to_leicester(player, bank, players):
    print("Advance to Leicester Square! If you pass Go, collect $200")
    move_player(player, target_index=26, collect_go=True)

def advance_to_mayfair(player, bank, players):
    print("Advance to mayfair! If you pass Go, collect $200")
    move_player(player, target_index=26, collect_go=True)

def advance_to_nearest_rr(player, bank, players):
    rr_index = nearest_rr(player.position)
    rr_name = board[rr_index].name
    print(f"Advance to the nearest railroad! The nearest railroad is {rr_name}! If you pass Go, collect $200")
    move_player(player, target_index=rr_index, collect_go=True)

def advance_to_nearest_util(player, bank, players):
    util_index = nearest_utility(player.position)
    move_player(player, target_index=util_index, collect_go=True)

def go_back_3_spaces(player, bank, players):
    print("Go back 3 spaces! If you pass Go, do not collect $200")
    move_player(player, target_index=(player.position - 3))

def bank_pays_divident(player, bank, players):
    print("Bank pays you a dividend of $50!")
    bank.transaction(sender=bank, receiver=player, amount=50)

def get_out_of_jail(player, bank, players):
    print("Get out of jail free card! You may keep this card until you want to use it.")
    player.escape_jail = True

def general_repairs(player, bank, players):
    print("Make general repairs on all your property. For each house pay $25, for each hotel pay $100.")
    house_count = 0
    hotel_count = 0
    for property in player.properties:
        if isinstance(property, Property):
            if property.house_number != 5:
                house_count += property.house_number
            else:
                hotel_count += 1
    amount = (house_cost * 25) + (hotel_cost * 100)
    bank.transaction(sender=player, receiver=bank, amount=amount)

def speeding_fine(player, bank, players):
    print("You have been fined $15 for speeding.")
    bank.transction(sender=player, receiver=bank, amount=15)

def advance_kcs(player, bank, players):
    print("Take a trip to King's Cross Station! If you pass Go, collect $200")
    move_player(player, target_index=5, collect_go=True)

def chairman(player, bank, players):
    print("You have been elected Chairman of the Board. Pay each player $50.")
    for p in players:
        if p != player:
            bank.transaction(sender=player, receiver=p, amount=50)

def matured_loan(player, bank, players):
    print("Your building loan matures. Collect $150.")
    bank.transaction(sender=bank, receiver=player, amount=150)

class ChanceDeck:
    def __init__(self, cards):
        self.cards = cards
