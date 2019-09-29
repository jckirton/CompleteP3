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
