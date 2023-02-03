import os
import time


def table(arr):
    print(" {} | {} | {}          1 | 2 | 3".format(arr[1], arr[2], arr[3]))
    print("---|---|---        ---|---|---")
    print(" {} | {} | {}          4 | 5 | 6 ".format(arr[4], arr[5], arr[6]))
    print("---|---|---        ---|---|---")
    print(" {} | {} | {}          7 | 8 | 9 ".format(arr[7], arr[8], arr[9]))


def check_winner(arr, sym):
    if (
        (arr[1] == sym and arr[2] == sym and arr[3] == sym)
        or (arr[4] == sym and arr[5] == sym and arr[6] == sym)
        or (arr[7] == sym and arr[8] == sym and arr[9] == sym)
        or (arr[1] == sym and arr[4] == sym and arr[7] == sym)
        or (arr[2] == sym and arr[5] == sym and arr[8] == sym)
        or (arr[3] == sym and arr[6] == sym and arr[9] == sym)
        or (arr[1] == sym and arr[5] == sym and arr[9] == sym)
        or (arr[3] == sym and arr[5] == sym and arr[7] == sym)
    ):
        return True
    return False


def check_full_table(arr):
    for i in range(1, 10):
        if check_space(arr, i):
            return False
    return True


def player_input():
    sym = " "
    while sym != "X" and sym != "O":
        sym = input("Player1: Choose X or O: ").upper()

    if sym == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def choose_first(player1_sym):
    if player1_sym == "X":
        return "Player 1"
    else:
        return "Player 2"


def player_choice(arr):
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_space(arr, pos):
        pos = int(input("Choose a position between (1-9): "))

    return pos


def check_space(arr, pos):
    return arr[pos] == " "


def place_sym(arr, sym, pos):
    arr[pos] = sym


def again():
    choice = input("Play again? (Y/N): ").upper()
    return choice.startswith("Y")


while True:
    os.system("CLS")
    arr = [" "] * 10
    player1_sym, player2_sym = player_input()

    turn = choose_first(player1_sym)
    print(turn + " will go first")
    for i in range(3, 0, -1):
        print(str(i) + "...")
        time.sleep(1)

    while True:
        os.system("CLS")
        if turn == "Player 1":
            table(arr)
            position = player_choice(arr)
            place_sym(arr, player1_sym, position)

            if check_winner(arr, player1_sym):
                os.system("CLS")
                table(arr)
                print("PLAYER 1 HAS WON!")
                break

            else:
                if check_full_table(arr):
                    os.system("CLS")
                    table(arr)
                    print("TIE GAME!")
                    break

                else:
                    turn = "Player 2"

        else:
            table(arr)
            position = player_choice(arr)
            place_sym(arr, player2_sym, position)

            if check_winner(arr, player2_sym):
                os.system("CLS")
                table(arr)
                print("PLAYER 2 HAS WON!")
                break

            else:
                if check_full_table(arr):
                    os.system("CLS")
                    table(arr)
                    print("TIE GAME!")
                    break

                else:
                    turn = "Player 1"

    if not again():
        break
