import random
import time

LOW_QUESTION = "Low number please.\n"
HIGH_QUESTION = "High number please.\n"


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


def get_num(question):
    num = None
    while type(num) is not int:
        try:
            num = int(input(question))
        except ValueError:
            print("Please choose a number.")

    return num


def get_guess(low_num, high_num):
    guess_num = None
    while guess_num not in list(range(low_num, high_num + 1)):
        try:
            guess_num = int(
                input(
                    f"Please guess a number between {low_num} and {high_num}.\nPress CTRL + C to quit at any time.\n"
                )
            )
            # if guess_num in "i give up":
            # print(f"Awww, you were so close!\nThe number was {num_to_guess}.")
            # replay()
            if guess_num not in list(range(low_num, high_num + 1)):
                raise IndexError
        except IndexError:
            print(f"Not between {low_num} and {high_num}.")
        except ValueError:
            print("Please choose a number.")

    return guess_num


def play():

    while True:
        print("\n" * 100)
        print("Hello and welcome to Number Guess!")
        print("A production by Ben and son, a coding family.")
        first_num = get_num(LOW_QUESTION)
        print("\n" * 100)
        second_num = get_num(HIGH_QUESTION)
        print("\n" * 100)
        while first_num == second_num:
            print("Please put in two differnt numbers")
            second_num = get_num(HIGH_QUESTION)
        low_num = first_num if first_num < second_num else second_num
        high_num = first_num if first_num > second_num else second_num
        num_to_guess = random.randint(low_num, high_num)
        guess_num = None

        while guess_num != num_to_guess:
            guess_num = get_guess(low_num, high_num)
            if guess_num < num_to_guess:
                print("\n" * 100)
                print("Higher")
            elif guess_num > num_to_guess:
                print("\n" * 100)
                print("Lower")

        print("\n" * 100)
        print("Hooray! Good job.👍")
        print(f"The number was {num_to_guess}")

        if not replay():
            print("Thanks for playing!")
            time.sleep(1.5)
            print("\n" * 100)
            break


if __name__ == "__main__":
    play()
