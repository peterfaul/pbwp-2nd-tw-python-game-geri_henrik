import string
import random
import sys

ship_type_database = {"Carrier": 4, "Battleship": 5, "Cruiser": 3, "Destroyer": 2, "Rambo": 1}

missmsg = ["Damn it, next time!", "Put on your glasses!", "Watch out!", "Missed..."]
hitmsg = ["Nice shot!", "You rock!", "It hurts!", "Ouch!"]

player1 = input("Please state your name: ")
player2 = input("Please state your name: ")
shoot_count_tracker = [0, 0]

player1_start_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}
player2_start_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}
player1_shoot_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}
player2_shoot_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}

row_index_letter = list(string.ascii_lowercase[:10])

def ship_placement(ship_type_database, start_grid):
    while True:
        try:
            for key, value in sorted(ship_type_database.items()):
                ship_direction_input = input("Do you want to place your {0} horizontally or vertically? It occupies {1} coordinates. ".format(key, value))
                beginning_coordinate_input = input("Beginning coordinates of your {0}: ".format(key))
                beginning_coordinate_key = beginning_coordinate_input[0]
                beginning_coordinate_value = int(beginning_coordinate_input[1:]) - 1

                if ship_direction_input[0] == "h":
                    for i in range(value):
                        if start_grid[beginning_coordinate_key][i+beginning_coordinate_value] == " 0 ":
                            start_grid[beginning_coordinate_key][i+beginning_coordinate_value] = " " + str(value) + " "
                        else:
                            raise ValueError
                    for k, v in sorted(start_grid.items()):
                         print(k,v)
                elif ship_direction_input[0] == "v":
                    for letter in row_index_letter[row_index_letter.index(beginning_coordinate_key):row_index_letter.index(beginning_coordinate_key)+value]:
                        if start_grid[letter][beginning_coordinate_value] == " 0 ":
                            start_grid[letter][beginning_coordinate_value] = " " + str(value) + " "
                        else:
                            raise ValueError
                    for k, v in sorted(start_grid.items()):
                         print(k,v)
        except:
            print("Oops, it seems you made a mistake. Please try again.")
            continue

ship_placement(ship_type_database, player1_start_grid)
ship_placement(ship_type_database, player2_start_grid)

def player_turn(start_grid, shoot_grid, player, tracker):
    global shoot_count_tracker
    while True:
        print("{0}'s turn".format(player))
        beginning_coordinate_input = input("Where do you want to shoot? ")
        beginning_coordinate_key = beginning_coordinate_input[0]
        beginning_coordinate_value = int(beginning_coordinate_input[1:]) -1

        if start_grid[beginning_coordinate_key][beginning_coordinate_value] != " 0 ":
            shoot_grid[beginning_coordinate_key][beginning_coordinate_value] = " X "
            print(hitmsg[random.randint(0, 3)])
            for k, v in sorted(shoot_grid.items()):
                 print(k,v)
            shoot_count_tracker[tracker] += 1
            if shoot_count_tracker[0] == 15:
                print("{0} winner pirate!".format(player1))
                sys.exit()
            elif shoot_count_tracker[1] == 15:
                print("{0} winner pirate!".format(player2))
                sys.exit()
            continue
        else:
            print(missmsg[random.randint(0, 3)])
            shoot_grid[beginning_coordinate_key][beginning_coordinate_value] = " I "
            for k, v in sorted(shoot_grid.items()):
                 print(k,v)
            break

while True:
    player_turn(player2_start_grid, player1_shoot_grid, player1, 0)
    player_turn(player1_start_grid, player2_shoot_grid, player2, 1)
