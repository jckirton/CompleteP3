"""
Creates a playable tic tac toe game.
"""
import random
import time


# import pysnooper
class TerminalColors:
    """
    A variety of colors to use for your terminal.
    """

    grey = "\033[1;30;40m"
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    blue = "\033[1;34;40m"
    magenta = "\033[1;35;40m"
    cyan = "\033[1;36;40m"
    white = "\033[1;37;40m"
    regular = "\033[1;37;40m"


tc = TerminalColors()


def display_board(board):
    """
    Creates and displays a tic tac toe board.
    """
    print("\n" * 100)
    print(
        f"{tc.grey}7{tc.regular}    |{tc.grey}8{tc.regular}    |{tc.grey}9{tc.regular}   "
    )
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + " ")
    print("     |     |    ")
    print("-----|-----|-----")
    print(
        f"{tc.grey}4{tc.regular}    |{tc.grey}5{tc.regular}    |{tc.grey}6{tc.regular}  "
    )
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + " ")
    print("     |     |    ")
    print("-----|-----|-----")
    print(
        f"{tc.grey}1{tc.regular}    |{tc.grey}2{tc.regular}    |{tc.grey}3{tc.regular}  "
    )
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + " ")
    print("     |     |    ")


def player_input():
    """
    Allows player 1 to choose wether to have X or O as their piece on the board.
    """
    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player 1 plz choose X or O: ").upper()

        player1 = (f"{tc.red}{marker}{tc.regular}", 1)

        if "X" in player1[0]:
            player2 = (f"{tc.cyan}O{tc.regular}", 2)
        else:
            player2 = (f"{tc.cyan}X{tc.regular}", 2)

    print("Player 1 is {} and Player 2 is {}".format(player1[0], player2[0]))
    return player1, player2


def place_marker(board, marker, position):
    """
    Places the player's piece on the board.
    """
    board[position] = marker


def win_check(board, mark):
    """
    Checks if a player has won or not.
    """
    if board[7] == board[8] == board[9] == mark:
        return True

    if board[1] == board[2] == board[3] == mark:
        return True

    if board[4] == board[5] == board[6] == mark:
        return True

    if board[7] == board[4] == board[1] == mark:
        return True

    if board[8] == board[5] == board[2] == mark:
        return True

    if board[9] == board[6] == board[3] == mark:
        return True

    if board[7] == board[5] == board[3] == mark:
        return True

    if board[9] == board[5] == board[1] == mark:
        return True

    else:
        return False


def choose_first():
    """
    Chooses which player goes first.
    """
    if random.randint(0, 1):
        return True
    else:
        return False

    # return True if random.randint(0, 1) else False


def space_check(board, position):
    """
    Checks if the space that the player is trying to put his or her marker is free.
    """
    if "X" not in board[position] and "O" not in board[position]:
        return True
    else:
        print("Space taken. Choose another")
        return False


def full_board_check(board):
    """
    Checks if the board is full.
    """
    for index in range(1, len(board)):
        if "X" not in board[index] and "O" not in board[index]:
            return False

    return True


def player_choice(board, player):
    """
    Asks the player where they would like to place there marker.
    """
    position = None
    while position not in [1 - 9]:
        try:
            position = int(input(f"Player {player[1]} choose a position from 1-9: "))
            if space_check(board, position):
                return position
        except ValueError:
            print("plz choose a number")
        except IndexError:
            print("plz choose only 1-9")


def replay():
    """
    Restarts the game.
    """
    while True:
        check = input("Would you like to play again? ").lower()
        if check in "no":
            print("Thanks For Playing!")
            time.sleep(1.5)
            print("\n" * 100)
            return False
        elif check in "yes":
            print("\n" * 100)
            return True
        else:
            print("yes or no?")
            time.sleep(1)


def loading():
    """
    Creates a false loading screen.
    """
    wait = random.randint(1, 10)
    print("\nLoading Now")
    print(f"Estimated Wait: {wait} second{'' if wait == 1 else 's'}")
    time.sleep(wait)


def play():
    """
    Starts the tic tac toe game.
    """
    while True:
        print("\n" * 100)
        print("Welcome to tic tac toe!")
        # default board
        board = ["#"] + [" "] * 9
        # alternate board
        # board = ["#"]
        # for index in range(1, 10):
        #     board.append(str(index))

        player1, player2 = player_input()

        game_on = True

        loading()

        while game_on:

            marker = player1[0]
            display_board(board)
            position = player_choice(board, player1)

            if space_check(board, position):
                place_marker(board, marker, position)
            display_board(board)

            if win_check(board, marker):
                print("Player 1 wins!!!")
                break
            if full_board_check(board):
                print("the board is full. nobody won.")
                break
            marker = player2[0]
            position = player_choice(board, player2)

            if space_check(board, position):
                place_marker(board, marker, position)
            display_board(board)

            if win_check(board, marker):
                print("Player 2 wins!!!")
                break
            if full_board_check(board):
                print("the board is full. nobody won.")
                break

        if not replay():
            time.sleep(3)
            break


if __name__ == "__main__":
    play()
else:
    while True:
        p = input("would you like to play?\n").lower()
        if p in "no":
            print("ok")
            time.sleep(1)
            print("\n" * 100)
            break
        elif p in "yes":
            play()
        else:
            print("yes or no?")
            time.sleep(1)
