"""
A redux of my tic tac toe game, now using objects!
"""

from time import sleep
from copy import copy
from colorama import Fore

DEFAULT = """7    |8    |9
  %s  |  %s  |  %s
     |     |
-----|-----|-----
4    |5    |6
  %s  |  %s  |  %s
     |     |
-----|-----|-----
1    |2    |3
  %s  |  %s  |  %s
     |     |     """


class Piece:
    """
    A tic tac toe piece, comprised of a single-character representation on the board, and the piece's age.

    marker: A single-character string that represents the piece on the playspace.
    position: the position of the piece on the playspace.
    """

    def __init__(self, marker: str, position: int):
        self.marker = marker
        self.position = position
        self.age = 0

    def age_piece(self):
        self.age += 1

    def __str__(self):
        if self.age == 1:
            return f"{Fore.YELLOW}{self.marker}{Fore.RESET}"
        if self.age == 2:
            return f"{Fore.RED}{self.marker}{Fore.RESET}"
        return self.marker


class Board:
    """
    The tic tac toe board.

    board_style_source: Optional input for an alternative board style source's relative file path.
    """

    def __init__(self, board_style_source: str | None = None):
        self.state: dict[int, Piece | None] = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
        }
        # if board_style_source:
        #     pass

    def reset(self):
        self.state = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
        }

    def __str__(self):
        # return f"{self.state}"
        # return self.display
        pos = copy(self.state)
        for i in pos:
            if pos[i] is None:
                pos[i] = " "

        display = DEFAULT % tuple(pos[i] for i in [7, 8, 9, 4, 5, 6, 1, 2, 3])

        return display


class Player:
    """
    Tic tac toe player, and their piece.
    """

    def __init__(self, marker: str, id: str):
        self.marker = marker
        self.id = id

    def place_piece(self, board: Board, position: int):
        board.state[position] = Piece(self.marker, position)


class Game:
    def __init__(self, board: Board, players: list[Player]):
        self.board = board
        self.players = players
        self.game_on: bool

    class GameManager:
        def __init__(self, age: bool = False):
            self.age = age

        def check_full(self, board: Board) -> bool:
            for pos in board.state:
                if board.state[pos] is None:
                    return False
            return True

        def check_win(self, board: Board, player: Player) -> bool:
            win_conditions = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
                [7, 5, 3],
                [1, 5, 9],
            ]

            for cond in win_conditions:
                null_check = False
                for pos in cond:
                    if board.state[pos] is None:
                        null_check = True
                if null_check:
                    pass
                elif (
                    board.state[cond[0]].marker
                    == board.state[cond[1]].marker
                    == board.state[cond[2]].marker
                    == player.marker
                ):
                    return True
            return False

        def age_pieces(self, board: Board, player: Player):
            for pos in board.state:
                try:
                    if board.state[pos].marker == player.marker:
                        board.state[pos].age_piece()
                    if board.state[pos].age >= 3:
                        board.state[pos] = None
                except AttributeError:
                    pass

        def do_turn(self, board: Board, player: Player):
            while True:
                try:
                    print("\n" * 100)
                    print(board)
                    move = int(input(f"\n{player.id}, choose a space: "))
                    # print(board.state[move])
                    if board.state[move] is not None:
                        print("Space taken, choose another.")
                        sleep(1.5)
                    else:
                        if self.age:
                            self.age_pieces(board, player)
                        player.place_piece(board, move)
                        break

                except (ValueError, KeyError):
                    print("Input not valid. Try again.")
                    sleep(1.5)

        def reset_board(self, board: Board):
            board.reset()

    def replay(self):
        from random import randint

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
                return bool(randint(0, 1))
            # When an invalid response is given, the user is prompted again.
            else:
                print("Yes or no?")
                sleep(1)

    def play(self, decay: bool = False):
        game_manager = self.GameManager(age=decay)
        self.game_on = True

        while self.game_on:
            for p in self.players:
                game_manager.do_turn(self.board, p)
                if game_manager.check_win(self.board, p):
                    print(("\n" * 100) + f"{self.board}\n\n{p.id} won.")
                    self.game_on = False
                    break
                if game_manager.check_full(self.board):
                    print(
                        ("\n" * 100) + f"{self.board}\n\nThe board is full, nobody won."
                    )
                    self.game_on = False
                    break
            if self.game_on is False:
                if self.replay():
                    self.game_on = True
                    game_manager.reset_board(self.board)


def play():
    game = Game(
        Board(),
        [Player("X", "P1"), Player("O", "P2")],
    )
    decay = (
        input("Should the pieces decay?\n").lower().strip()
    )  # prevents windows fuckery

    if decay in "no":
        game.play()
    elif decay in "yes":
        game.play(True)


if __name__ == "__main__":
    play()
