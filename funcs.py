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
    import random

    while True:
        check = input("Would you like to play again? ").lower()
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
    import time

    print("Sorry this function is broken :(\n       [Error No. 5]")
    while True:
        deats = input("Detals?\n").lower()
        if deats in "no":
            print("Plz call [insert number here] to let then know.")
            break
        elif deats in "yes":
            print(f"{og_func} is no longer functional.")
            print("Plz call [insert number here] to let then know.")
            break
        else:
            print("Yes or no?")
            time.sleep(1.5)
