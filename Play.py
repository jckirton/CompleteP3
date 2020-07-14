from games import tic_tac_toe, blackjack, num_guess, num_guess_V2
import time
from funcs import TerminalColors

tc = TerminalColors()


while True:
    print(f"{tc.regular}\n" * 100)
    game = input(
        f"Which game would you like to play?\n\n{tc.green}1: Tic Tac Toe\n{tc.magenta}2: Blackjack\n{tc.red}3: Number Guess V1\n{tc.cyan}4: Number Guess V2{tc.regular}\n\n"
    )
    print(f"{tc.regular}")
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
        print("Ok, Cya!\n\n-Jackson Kirton")
        time.sleep(2.5)
        print("\n" * 100)
        break
