import string
import random
import sys
import os
import time

ship_type_database = {4: "Carrier" , 5: "Battleship", 3: "Cruiser", 2: "Destroyer", 1: "Rambo"}
missmsg = ["Damn it, next time!", "Put on your glasses!", "Watch out!", "Missed...", "Buzadara"]
hitmsg = ["Nice shot!", "You rock!", "It hurts!", "Ouch!", "Surefire"]
player1 = input("Please state your name: ")
player2 = input("Please state your name: ")
os.system("clear")
shoot_count_tracker = [0, 0]
sunken_ship_tracker = [[], []]
top_line = ["   " + str(i) + "   " for i in list(range(1, 11))]
player1_start_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}
player2_start_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}
player1_shoot_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}
player2_shoot_grid = {key:[" 0 "] * 10 for key in string.ascii_lowercase[:10]}
row_index_letter = list(string.ascii_lowercase[:10])

def print_grid(current_grid):
    print("  " + "".join(top_line))
    for k, v in sorted(current_grid.items()):
         print('{0}: {1}'.format(k,v))

def ship_placement(player, ship_type_database, start_grid):
    for key, value in sorted(ship_type_database.items(), reverse=True):
        while True:
            try:
                print("{0}'s turn".format(player))
                print_grid(start_grid)
                ship_direction_input = input("Do you want to place your {0} horizontally or vertically? It occupies {1} coordinates.: ".format(value, key))
                beginning_coordinate_input = input("Beginning coordinates of your {0}: ".format(value))
                beginning_coordinate_key = beginning_coordinate_input[0]
                beginning_coordinate_value = int(beginning_coordinate_input[1:]) - 1

                if ship_direction_input[0] == "h":
                    check_ship = []
                    for i in range(key):
                        check_ship.append(start_grid[beginning_coordinate_key][i+beginning_coordinate_value])
                        if not " 0 " in check_ship:
                            raise ValueError
                        else:
                            start_grid[beginning_coordinate_key][i+beginning_coordinate_value] = " " + str(key) + " "
                elif ship_direction_input[0] == "v":
                    check_ship = []
                    for letter in row_index_letter[row_index_letter.index(beginning_coordinate_key):row_index_letter.index(beginning_coordinate_key)+key]:
                        check_ship.append(start_grid[letter][beginning_coordinate_value])
                        if not " 0 " in check_ship:
                            raise ValueError
                        else:
                            start_grid[letter][beginning_coordinate_value] = " " + str(key) + " "
                break
            except:
                print("It seems you made a mistake, please try your input again!")
                time.sleep(2)
                os.system("clear")
                continue

        os.system("clear")

ship_placement(player1, ship_type_database, player1_start_grid)
ship_placement(player2, ship_type_database, player2_start_grid)

def player_turn(start_grid, shoot_grid, player, tracker):
    global shoot_count_tracker
    hit = True
    while hit == True:
        while True:
            try:
                print_grid(shoot_grid)
                print("{0}'s turn".format(player))
                beginning_coordinate_input = input("Where do you want to shoot? ")
                beginning_coordinate_key = beginning_coordinate_input[0]
                beginning_coordinate_value = int(beginning_coordinate_input[1:]) -1

                if start_grid[beginning_coordinate_key][beginning_coordinate_value] != " 0 " and shoot_grid[beginning_coordinate_key][beginning_coordinate_value] != " X ":
                    shoot_grid[beginning_coordinate_key][beginning_coordinate_value] = " X "
                    print(hitmsg[random.randint(0, 4)])

                    ship_num = int(start_grid[beginning_coordinate_key][beginning_coordinate_value].strip())
                    sunken_ship_tracker[tracker].append(ship_num)
                    if ship_num == sunken_ship_tracker[tracker].count(ship_num):
                        print("You sunk {0}".format(ship_type_database[ship_num]))
                    hit = True
                    shoot_count_tracker[tracker] += 1
                    if shoot_count_tracker[0] == 15:
                        print("{0} winner pirate!".format(player1))
                        raise NameError
                    elif shoot_count_tracker[1] == 15:
                        print("{0} winner pirate!".format(player2))
                        raise NameError
                    time.sleep(2)
                    os.system("clear")
                    continue
                elif start_grid[beginning_coordinate_key][beginning_coordinate_value] != " 0 " and shoot_grid[beginning_coordinate_key][beginning_coordinate_value] == " X ":
                    print ("You fucking bastard, you prick, you have already tried to shoot here!")
                    hit = False
                    time.sleep(2)
                    os.system("clear")
                    break
                else:
                    print(missmsg[random.randint(0, 4)])
                    shoot_grid[beginning_coordinate_key][beginning_coordinate_value] = " I "
                    hit = False
                    time.sleep(2)
                    os.system("clear")
                    break
                break
            except NameError:
                sys.exit()
            except:
                print("You fuck, you misstyped the coordinate")
                time.sleep(2)
                os.system("clear")
                continue

while True:
    player_turn(player2_start_grid, player1_shoot_grid, player1, 0)
    player_turn(player1_start_grid, player2_shoot_grid, player2, 1)
