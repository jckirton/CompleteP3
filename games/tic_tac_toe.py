"""
A playable game of tic tac toe.
"""

import random
import time


def display_board(board: list[str]):
    """
    Takes the current game board state and displays it.

    board: The current board state. A list of strings of length 10, with index 0 being "#", and index 1-9 being the respective board positions.
    """
    # "Clearing" the terminal screen by printing a whole lot of new lines.
    print("\n" * 100)
    # Printing the board.
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


def player_input() -> tuple[tuple[str, int], tuple[str, int]]:
    """
    Asks player 1 to choose between "X" and "O" for their board marker, and returns the players' information.

    Player information returned as in the format: (player1=(marker, 1), player2=(marker, 2))
    """
    # Defining marker as an empty string.
    marker = ""

    # Getting the player's choice. Contained within a while loop to repeat the question if an invalid answer is given.
    while marker != "X" and marker != "O":
        # Getting player input.
        marker = input("Player 1 please choose X or O: ").upper()

        # Defining player 1 information based on the given input.
        player1 = (f"{marker}", 1)

        # Defining player 2 information based on what player 1 chose.
        if player1[0] == "X":
            player2 = ("O", 2)
        elif player1[0] == "O":
            player2 = ("X", 2)
        # Or clearing the terminal to prompt again if an invalid choice was given.
        else:
            print("\n" * 100)

    # Stating what the player information is and returning the player information.
    print(f"Player 1 is {player1[0]} and Player 2 is {player2[0]}")
    return player1, player2


def place_marker(board: list, marker: str, position: int):
    """
    Updates the board state based on the supplied information.
    In practice, this is the player's chosen move.

    board: The current board state. A list of strings of length 10, with index 0 being "#", and index 1-9 being the respective board positions.
    marker: The player's marker.
    position: The player's chosen position.
    """
    board[position] = marker


def win_check(board: list, mark: str) -> bool:
    """
    Checks the board state for a win condition of the supplied player marker.

    board: The board state. A list of strings of length 10, with index 0 being "#", and index 1-9 being the respective board positions.
    mark: The player marker being checked.
    """
    # Brute forcing win condition checks, returning True if a win condition is met, or False if not.
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


def space_check(board: list, position: int) -> bool:
    """
    Checks if the supplied board position is empty, and returns True if it is.

    board: Current board state. A list of strings of length 10, with index 0 being "#", and index 1-9 being the respective board positions.
    position: Chosen position being checked for avalability.
    """
    # Checking that there are no player markers or filler markers in the supplied position.
    if (
        "X" not in board[position]
        and "O" not in board[position]
        # Check for "filler" marker is made as the board looks like this:
        # ["#", "pos1", "pos2", "pos3", ...]
        # This decision is made so that in code I can reference board position 1 as board[1].
        and "#" not in board[position]
    ):
        return True
    else:
        print("Space taken. Choose another")
        return False


def full_board_check(board: list):
    """
    Checks if the board is full.

    board: Current board state. A list of strings of length 10, with index 0 being "#", and index 1-9 being the respective board positions.
    """
    # Checking every index in the board state from 1-9 for player markers. If an empty space is found, returns False.
    for index in range(1, len(board)):
        if "X" not in board[index] and "O" not in board[index]:
            return False

    return True


def player_choice(board: list, player: tuple[str, int]):
    """
    Asks the player where they would like to place their marker, and checks if that choice is valid.

    board: Current board state. A list of strings of length 10, with index 0 being "#", and index 1-9 being the respective board positions.
    player: The player information. Contains the player's marker and "player number".
    """
    position = None
    # Function code is contained in a while loop as there is error and space checking, allowing the prompt to be run again when an error is caught.
    while position not in [1 - 9]:
        # A try-except block to catch and handle errors, instead of crashing the code.
        try:
            # Getting the input and converting it from a string to an int. If the player inputs something other than an int, a ValueError is thrown here.
            position = int(input(f"Player {player[1]} choose a position from 1-9: "))
            # Special checking if the player chooses position 0, then displaying IndexError text instead of "space taken" text.
            # This is done as there technically is a board[0], meaning no IndexError will be thrown later.
            if position == 0:
                print("Please choose only 1-9")
                time.sleep(1.5)
                print("\n" * 100)
                display_board(board)
                continue
            # Checking if the chosen space if free, and returning the chosen position if so.
            # If the player chooses a position that doesn't exist, like 10, an IndexError is thrown, as board[10] does not exist.
            if space_check(board, position):
                return position
        # Catches when a ValueError is thrown, and handles it accordingly.
        except ValueError:
            # Requests the player to choose a number, then displays the board and prompt again.
            print("Please choose a number")
            time.sleep(1.5)
            print("\n" * 100)
            display_board(board)
        # Catches when an IndexError is thrown, and handles it accordingly.
        except IndexError:
            # Requests the player to choose a number within the acceptible range, then displays the board and prompt again.
            print("Please choose only 1-9")
            time.sleep(1.5)
            print("\n" * 100)
            display_board(board)


def replay():
    """
    Asks the player if they would like to play again, and returns True if so.
    """
    # Prompt is contained within a loop to allow the user to be prompted again upon an invalid response.
    while True:
        # The replay prompt and input.
        # The "lower" method is used to convert all the characters to lowercase, allowing checks to work as intended as "in" and "==" statements are case sensitive.
        check = input(
            'Would you like to play again?\nType "maybe" or "?" to leave it up to the computer.\n'
        ).lower()
        # Checks if the user's response was "no", "yes", or "maybe?", using the "in" statement to allow inputs such as "y", "n", "m", and "?" to handle correctly.
        # "no" is checked first as the in statement also returns true from an empty string, meaning that if enter is pressed with no supplied text, "no" is chosen.
        if check in "no":
            return False
        elif check in "yes":
            print("\n" * 100)
            return True
        elif check in "maybe?":
            # If the user decides to leave it up to the computer, there is a 50/50 chance the game will begin again.
            # This is achieved due to data in python having "truethy" and "falsey" values.
            # In this case, 0 has a "falsey" value, meaning that the bool method will return false. 1 is the inverse, with it having a "truethy" value.
            return bool(random.randint(0, 1))
        # When an invalid response is given, the user is prompted again.
        else:
            print("Yes or no?")
            time.sleep(1)


def play():
    """
    Starts and runs the tic tac toe game.
    """
    # All game code is contained within a loop to allow the user to restart the game upon game end.
    while True:
        # Terminal "clearing" and welcome screen.
        print("\n" * 100)
        print("Welcome to tic tac toe!")
        print("A production by Ben and son, a coding family.")

        # Defining initial board state.
        # The board state looks like this: ["#", "pos1", "pos2", "pos3", ...]
        # This decision is made so that in code I can reference board position 1 as board[1], and so on.
        # This decision makes both reading the code and position input handling much easier.
        board = ["#"] + [" "] * 9

        # Gathering and defining player information.
        player1, player2 = player_input()

        # The actual gameplay loop.
        while True:
            # Beginning player 1's turn and setting current marker to player 1's marker.
            marker = player1[0]
            # Displaying the game board.
            display_board(board)
            # Getting current player 1's move.
            position = player_choice(board, player1)
            # Updating board state and displaying updated board.
            place_marker(board, marker, position)
            display_board(board)

            # Checking for game end conditions and ending game if so.
            if win_check(board, marker):
                print("Player 1 wins!")
                break
            if full_board_check(board):
                print("The board is full. Nobody won.")
                break

            # Player 2's turn. Identical to player 1's turn, just with player 2's information.
            marker = player2[0]
            position = player_choice(board, player2)

            place_marker(board, marker, position)
            display_board(board)

            if win_check(board, marker):
                print("Player 2 wins!")
                break
            if full_board_check(board):
                print("The board is full. Nobody won.")
                break
            # Gameplay now loops if no end condition has been met.

        # Upon gameplay end, asks the user if they would like to play again. If yes, doesn't exit the loop.
        if not replay():
            # If no, exits the game loop.
            print("Thanks for playing!")
            time.sleep(1.5)
            print("\n" * 100)
            break


# Fancy thing for running the game if the tic_tac_toe file itself is being run.
# Also avoids the play function being run upon an import of the file.
if __name__ == "__main__":
    play()
