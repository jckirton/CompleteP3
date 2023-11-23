"""
Creates a playable tic tac toe game.
"""
import random
import time


def display_board(board):
    """
    Creates and displays a tic tac toe board.
    """
    print("\n" * 100)
    print("7    |8    |9   ")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + " ")
    print("     |     |    ")
    print("-----|-----|-----")
    print("4    |5    |6  ")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + " ")
    print("     |     |    ")
    print("-----|-----|-----")
    print("1    |2    |3  ")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + " ")
    print("     |     |    ")


def player_input():
    """
    Allows player 1 to choose whether to have X or O as their piece on the board.
    """
    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player 1 please choose X or O: ").upper()

        player1 = marker

        if player1 == "X":
            player2 = "O"
        elif player1 == "O":
            player2 = "X"
        else:
            print("\n" * 100)

    print(f"Player 1 is {player1} and Player 2 is {player2}.")
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


def space_check(board, position):
    """
    Checks if the space that the player is trying to put his or her marker is free.
    """
    if (
        "X" not in board[position]
        and "O" not in board[position]
    ):
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


def player_choice(
    board,
    player,
):
    """
    Asks the player where they would like to place there marker.
    """
    position = None
    while position not in [1 - 9]:
        try:
            position = int(input(f"Player {player[1]} choose a position from 1-9: "))
            if position == 0:
                print("Please choose only 1-9")
                time.sleep(1.5)
                print("\n" * 100)
                display_board(
                    board,
                )
                continue
            if space_check(board, position):
                return position
        except ValueError:
            print("Please choose a number")
            time.sleep(1.5)
            print("\n" * 100)
            display_board(
                board,
            )
        except IndexError:
            print("Please choose only 1-9")
            time.sleep(1.5)
            print("\n" * 100)
            display_board(
                board,
            )


def replay():
    """
    Restarts the game.
    """
    while True:
        check = input(
            'Would you like to play again?\nType "maybe" or "?" to leave it up to the computer. '
        ).lower()
        if check in "no":
            return False
        elif check in "yes":
            print("\n" * 100)
            return True
        elif check in "maybe?":
            return random.randint(0, 1)
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
        print("A production by Ben and son, a coding family.")
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
            marker = player1
            display_board(
                board,
            )
            position = player_choice(
                board,
                player1,
            )

            if space_check(board, position):
                place_marker(board, marker, position)
            display_board(
                board,
            )

            if win_check(board, marker):
                print("Player 1 wins!")
                break
            if full_board_check(board):
                print("The board is full. Nobody won.")
                break
            marker = player2
            position = player_choice(
                board,
                player2,
            )

            if space_check(board, position):
                place_marker(board, marker, position)
            display_board(
                board,
            )

            if win_check(board, marker):
                print("Player 2 wins!")
                break
            if full_board_check(board):
                print("The board is full. Nobody won.")
                break

        if not replay():
            print("Thanks for playing!")
            time.sleep(1.5)
            print("\n" * 100)
            break


if __name__ == "__main__":
    play()
