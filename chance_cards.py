from monopoly_game import board, move_player, nearest_rr, nearest_utility

def advance_to_go(player):
    print("Advance to Go!")
    move_player(player, target_index=0)

def go_to_jail(player):
    print("Go to Jail. Move directly to Jail, do not pass Go or collect $200.")
    player.in_jail = True
    player.turns_in_jail = 0
    move_player(player, target_index=10)

def advance_to_pallmall(player):
    print("Advance to Pall Mall! If you pass Go, collect $200!")
    move_player(player, target_index=11, collect_go=True)

def advance_to_trafalgar(player):
    print("Advance to Trafalgar Square! If you pass Go, collect $200")
    move_player(player, target_index=24, collect_go=True)

def advance_to_leicester(player):
    print("Advance to Leicester Square! If you pass Go, collect $200")
    move_player(player, target_index=26, collect_go=True)

def advance_to_mayfair(player):
    print("Advance to mayfair! If you pass Go, collect $200")
    move_player(player, target_index=26, collect_go=True)

def advance_to_nearest_rr(player):
    rr_index = nearest_rr(player.position)
    rr_name = board[rr_index].name
    print(f"Advance to the nearest railroad! The nearest railroad is {rr_name}! If you pass Go, collect $200")
    move_player(player, target_index=rr_index, collect_go=True)

def advance_to_nearest_util(player):
    util_index = nearest_utility(player.position)
    move_player(player, target_index=util_index, collect_go=True)

def go_back_3_spaces(player):
    print("Go back 3 spaces! If you pass Go, do not collect $200")
    move_player(player, target_index=(player.position - 3))

def bank_pays_divident(player):
    print("Bank pays you a dividend of $50!")
    player.money += 50
