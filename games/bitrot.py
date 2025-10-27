"""
A redux of my tic tac toe game, now using objects!
"""

from time import sleep
from copy import copy

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


class InvalidMove(Exception):
    pass


def input_with_timeout(prompt: str, timeout: int | float, error=TimeoutError):
    import select
    from sys import stdout, stdin

    stdout.write(prompt)
    stdout.flush()
    ready, _, _ = select.select([stdin], [], [], timeout)
    if ready:
        return stdin.readline().rstrip("\n")  # expect stdin to be line-buffered
    else:
        stdout.write("\n")
        stdout.flush()
        raise error


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
        self.AGE_COLORS = {
            "clear": "\x1b[0m",  # Clear
            "red": "\x1b[0;31m",  # Red
            "yellow": "\x1b[1;33m",  # Yellow
            "green": "\x1b[0;32m",
        }

    def age_piece(self):
        self.age += 1

    def __str__(self):
        if self.age == 1:
            return f"{self.AGE_COLORS["yellow"]}{self.marker}{self.AGE_COLORS["clear"]}"
        if self.age == 2:
            return f"{self.AGE_COLORS["red"]}{self.marker}{self.AGE_COLORS["clear"]}"
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
        def __init__(self):
            self.age = True

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
                    print("\n" * 20)
                    print(board)
                    try:
                        move = input_with_timeout(f"\n{player.id}, choose a space: ", 5)
                        move = int(move[-1])
                    except ValueError:
                        raise InvalidMove(f"move '{move}' is not a number")
                    except IndexError:
                        raise InvalidMove("empty move, turn passed")
                    except TimeoutError:
                        raise InvalidMove("move not made within time limit")
                    # print(board.state[move])
                    try:
                        if board.state[move] is not None:
                            raise InvalidMove(f"position {move} already filled")
                        else:
                            if self.age:
                                self.age_pieces(board, player)
                            player.place_piece(board, move)
                            break
                    except KeyError:
                        raise InvalidMove(f"position {move} not within board")

                except InvalidMove:
                    if self.age:
                        self.age_pieces(board, player)
                    break

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
                print("\n" * 20)
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

    def play(self):
        game_manager = self.GameManager()
        self.game_on = True

        while self.game_on:
            for p in self.players:
                game_manager.do_turn(self.board, p)
                if game_manager.check_win(self.board, p):
                    print(("\n" * 20) + f"{self.board}\n\n{p.id} won.")
                    self.game_on = False
                    break
                if game_manager.check_full(self.board):
                    print(
                        ("\n" * 20) + f"{self.board}\n\nThe board is full, nobody won."
                    )
                    self.game_on = False
                    break
            if self.game_on is False:
                if self.replay():
                    self.game_on = True
                    game_manager.reset_board(self.board)


def play():
    from os import system

    game = Game(
        Board(),
        [Player("0", "Defender (0)"), Player("1", "Attacker (1)")],
    )

    system("clear")

    input("Press enter to start game.\n")

    game.play()


if __name__ == "__main__":
    play()
