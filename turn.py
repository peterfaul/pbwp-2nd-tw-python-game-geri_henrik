def player_turn(grid):
    while True:
        beginning_coordinate_input = input("Where do you want to shoot? ")
        beginning_coordinate_key = beginning_coordinate_input[0]
        beginning_coordinate_value = int(beginning_coordinate_input[1:])

        if grid[beginning_coordinate_key][beginning_coordinate_value] != " 0 ":
            print("hit")
            continue
        else:
            break
