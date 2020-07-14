from games import tic_tac_toe, blackjack, num_guess, num_guess_V2
import time

while True:
    print("\n" * 100)
    game = input(
        "Which game would you like to play?\n\n1: Tic Tac Toe\n2: Blackjack\n3: Number Guess V1\n4: Number Guess V2\n\n"
    )

    if game == "1":
        tic_tac_toe.play()
    elif game == "2":
        blackjack.play()
    elif game == "3":
        num_guess.play()
    elif game == "4":
        num_guess_V2.play()
    else:
        print("\n" * 100)
        print("Ok, Cya!\n\n-Jackson")
        time.sleep(2.5)
        print("\n" * 100)
        break
