# Change your player to a dictionary with a key that holds onto where the player has been.
# Then, when drawing the map, show . for every cell they've been in.

import random

CELLS = [(0,0),(0,1),(0,2),(0,3),
        (1,0),(1,1),(1,2),(1,3),
        (2,0),(2,1),(2,2),(2,3),
        (3,0),(3,1),(3,2),(3,3)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    player = random.choice(CELLS)

    if monster == door or monster == player or door == player:
        return get_locations()

    return monster,door,player

def move_player(player,move):
    PREV_MOVES = [ ] # to save the previous positions of player
    # get the player's current location
    x,y = player["now"]
    PREV_MOVES.append(player["now"])

    if move == "LEFT":
        y -= 1
    elif move == "RIGHT":
        y += 1
    elif move == "UP":
        x -= 1
    elif move == "DOWN":
        x += 1

    player = x,y
    return player,PREV_MOVES

def get_moves(player):
    moves = ["LEFT","RIGHT","UP","DOWN"]
    # player = (x,y)
    if player["now"][1] == 0:
        moves.remove("LEFT")
    if player["now"][1] == 3:
        moves.remove("RIGHT")
    if player["now"][0] == 0:
        moves.remove("UP")
    if player["now"][0] == 3:
        moves.remove("DOWN")

    return moves

def draw_map():
    print(" _ _ _ _")
    tile = "|{}"

    for idx, cell in enumerate(CELLS):
        if idx in [0,1,2,4,5,6,8,9,10,12,13,14]:
            if cell == player["now"]:
                print(tile.format("x"), end="")
            elif cell in player['later']:
                print(tile.format("."), end="")
            else:
                print(tile.format("_"), end="")
        else:
            if cell == player["now"]:
                print(tile.format("x|"))
            elif cell in player['later']:
                print(tile.format(".|"))
            else:
                print(tile.format("_|"))

# player dictionary with current position = 'now' with 1 value and a list of previous positions = 'later'
player = {'now':'','later':[]}
monster,door,player["now"] = get_locations()
print("Welcome to the dungeon!")


while True:
    moves = get_moves(player)

    print("You're currently in room {}".format(player["now"]))

    draw_map()

    print("You can move {}".format(moves))
    print("Enter QUIT to quit.")

    move = input("> ")
    move = move.upper()

    if move == "QUIT":
        break

    if move in moves:
        player["now"],PREV_MOVES = move_player(player,move)
        # to not repeat the moves in the 'later' key in order to print the . later on
        if PREV_MOVES[0] not in player['later']:
            player['later'].append(PREV_MOVES[0])
    else:
        print("Walls are hard. Stop walking into them!")
        continue

    if player["now"] == door:
        print("You escaped!")
        break
    elif player["now"] == monster:
        print("You are eaten by the grue!")
        break
