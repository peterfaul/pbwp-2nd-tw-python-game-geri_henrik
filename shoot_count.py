
ship_type_database = {"Carrier": 4, "Battleship": 5, "Cruiser": 3, "Destroyer": 2, "Rambo": 1}
sunken_ship_tracker = [[5, 5, 5, 5, 5, 2, 4, 4, 4, 4], []]

for key, value in ship_type_database.items():
    if value == sunken_ship_tracker[0].count(value):
        print("You sunk {0}".format(key))
