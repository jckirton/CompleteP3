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
            return False
        elif check in "yes":
            print("\n" * 100)
            return True
        else:
            print("yes or no?")
            time.sleep(1)
