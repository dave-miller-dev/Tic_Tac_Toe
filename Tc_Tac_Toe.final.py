player_input = '_' * 9
player_input = list(player_input.replace("_", " "))
spaces_count = 0
coordinate_library = ['1', '2', '3']
restricted_library = ['4', '5', '6', '7', '8', '9']
x_counter = 0
o_counter = 0
x_game = False
o_game = False
x_state = False
o_state = False

for character in player_input:
    if character == " ":
        spaces_count += 1

for character in player_input:
    if character == "X":
        x_counter += 1
    elif character == "O":
        o_counter += 1


def print_screen():

    line1 = f"| {player_input[0]} {player_input[1]} {player_input[2]} |"
    line2 = f"| {player_input[3]} {player_input[4]} {player_input[5]} |"
    line3 = f"| {player_input[6]} {player_input[7]} {player_input[8]} |"
    print("-" * 9)
    print(line1)
    print(line2)
    print(line3)
    print("-" * 9)


def check_draw():
    if spaces_count == 0:
        print("Draw")


def check_finished():
    if not x_game:
        if not o_game:
            if spaces_count > 0:
                if abs(x_counter - o_counter) < 2:
                    print("Game not finished")


def check_impossible():
    if x_game and o_game:
        print("Impossible")
    elif abs(x_counter - o_counter) >= 2:
        print("Impossible")


def check_x():
    global x_game
    global o_game
    global x_counter

    if player_input[0] == "X":
        if player_input[1] == "X":
            if player_input[2] == "X":
                print("X wins")
                x_game = True
        elif player_input[2] == "X":
            if player_input[4] == "X":
                if player_input[6] == "X":
                    print("X wins")
                    x_game = True
        elif player_input[3] == "X":
            if player_input[6] == "X":
                x_game = True

        elif player_input[4] == "X":
            if player_input[8] == "X":
                print("X wins")
                x_game = True
    elif player_input[3] == "X":
        if player_input[4] == "X":
            if player_input[5] == "X":
                print("X wins")
                x_game = True
        elif player_input[6] == "X":
            x_game = True
    elif player_input[6] == "X":
        if player_input[7] == "X":
            if player_input[8] == "X":
                print("X wins")
                x_game = True


def check_o():
    global x_game
    global o_game
    global o_counter

    if player_input[0] == "O":
        if player_input[1] == "O":
            if player_input[2] == "O":
                print("O wins")
                o_game = True
            elif player_input[7] == "O":
                print("O wins")
                o_game = True
        elif player_input[2] == "O":
            if player_input[5] == "O":
                if player_input[8] == "O":
                    print("O wins")
                    o_game = True
            elif player_input[4] == "O":
                if player_input[6] == "O":
                    print("O wins")
                    o_game = True
        elif player_input[3] == "O":
            if player_input[6] == "O":
                o_game = True

        elif player_input[4] == "O":
            if player_input[8] == "O":
                print("O wins")
                o_game = True
    elif player_input[1] == "O":
        if player_input[4] == "O":
            if player_input[7] == "O":
                o_game = True
        elif player_input[2] == "O":
            if player_input[5] == "O":
                if player_input[8] == "O":
                    print("O wins")
                    o_game = True
    elif player_input[3] == "O":
        if player_input[4] == "O":
            if player_input[5] == "O":
                print("O wins")
                o_game = True
    elif player_input[6] == "O":
        if player_input[7] == "O":
            if player_input[8] == "O":
                print("O wins")
                o_game = True


print_screen()

while spaces_count != 0:
    if x_game:
        break
    elif o_game:
        break
    coordinates_string_input = input("Enter the coordinates: ").strip()
    coordinates_split_string = coordinates_string_input.split()
    if len(coordinates_split_string) == 2:
        check_draw()
        x, y = coordinates_split_string
        if x in restricted_library:
            print("Coordinates should be from 1 to 3!")
        elif y in restricted_library:
            print("Coordinates should be from 1 to 3!")
        elif x not in coordinate_library:
            print("You should enter numbers!")
        elif y not in coordinate_library:
            print("You should enter numbers!")
        elif x and y in coordinate_library:
            if x == '1':
                if y == '1':
                    if player_input[6] == " ":
                        if not x_state:
                            player_input[6] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[6] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
                elif y == '2':
                    if player_input[3] == " ":
                        if not x_state:
                            player_input[3] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[3] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
                elif y == '3':
                    if player_input[0] == " ":
                        if not x_state:
                            player_input[0] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[0] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
            elif x == '2':
                if y == '1':
                    if player_input[7] == " ":
                        if not x_state:
                            player_input[7] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[7] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
                elif y == '2':
                    if player_input[4] == " ":
                        if not x_state:
                            player_input[4] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[4] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
                elif y == '3':
                    if player_input[1] == " ":
                        if not x_state:
                            player_input[1] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[1] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
            elif x == '3':
                if y == '1':
                    if player_input[8] == " ":
                        if not x_state:
                            player_input[8] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[8] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
                elif y == '2':
                    if player_input[5] == " ":
                        if not x_state:
                            player_input[5] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[5] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
                elif y == '3':
                    if player_input[2] == " ":
                        if not x_state:
                            player_input[2] = "X"
                            spaces_count -= 1
                            x_state = True
                            o_state = False
                            print_screen()
                        elif x_state:
                            player_input[2] = "O"
                            spaces_count -= 1
                            o_state = True
                            x_state = False
                            print_screen()
                    else:
                        print("This cell is occupied! Choose another one!")
    elif len(coordinates_split_string) == 1:
        print("You should enter numbers!")
    check_draw()
    check_x()
    check_o()

