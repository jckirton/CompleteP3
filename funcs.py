def clear():
    print("\n" * 100)


def loading():
    """
    Creates a false loading screen.
    """
    # "Put at top."
    import time
    import random

    wait = random.randint(1, 10)
    # print("\n" * 100)
    print("\nLoading Now")
    print(f"Estimated Wait: {wait} second{'' if wait == 1 else 's'}")
    time.sleep(wait)
    # print("\n" * 100)


def replay():
    """
    Restarts the game.
    """
    import time

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


def func_breaker(og_func):
    print("Sorry this function is broken :(")
