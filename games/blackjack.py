"""
Creates and starts a playable and savable game of Blackjack.
"""
import random
import time

save_1 = ".chips"
save_2 = ".chips2"
save_3 = ".chips3"
total = 0
suits = ("❤️", "♦️", "⚜️", "♣️")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return f"The deck has: {deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    chosen_save = ""

    def __init__(self):
        self.bet = 0

    def save_chips(self):
        global total

        if self.chosen_save != "debug":
            total = round(total)
            with open(self.chosen_save, "w") as file:
                file.write(str(total))

    def win_bet(self, blackjack=False):
        global total
        # total += self.bet if not blackjack else (self.bet * 1.5)
        if blackjack and self.chosen_save != "debug":
            total += self.bet * 1.5
            total = round(total)
        else:
            total += self.bet

        self.save_chips()

    def lose_bet(self):
        global total
        mto = ""
        if (total - self.bet) > 1:
            mto = "s"
        if (total - self.bet) == 0:
            print("\nYour Out of Chips!\nGiving new chip stack.")
            total = 100
            self.save_chips()
        elif (total - self.bet) < 10:
            print(
                f"\n{total - self.bet} chip{mto} is not enough to continue!\nHere, take some of mine."
            )
            total = 100
            self.save_chips()
        else:
            total -= self.bet
            self.save_chips()


def choose_save(chips):
    global total
    try:
        with open(save_1, "r") as file:
            save1_total = str(int(float(file.read()))) + " Chips"
    except FileNotFoundError:
        save1_total = "No Save"
    except ValueError:
        save1_total = "Save Invalid"

    try:
        with open(save_2, "r") as file:
            save2_total = str(int(float(file.read()))) + " Chips"
    except FileNotFoundError:
        save2_total = "No Save"
    except ValueError:
        save2_total = "Save Invalid"

    try:
        with open(save_3, "r") as file:
            save3_total = str(int(float(file.read()))) + " Chips"
    except FileNotFoundError:
        save3_total = "No Save"
    except ValueError:
        save3_total = "Save Invalid"

    while True:
        print("\n" * 100)
        save = input(
            f"Which save would you like to use?\n1: {save1_total}\n2: {save2_total}\n3: {save3_total}\n"
        )

        if save == "1":
            chips.chosen_save = save_1
            print("\n" * 100)
            break
        elif save == "2":
            chips.chosen_save = save_2
            print("\n" * 100)
            break
        elif save == "3":
            chips.chosen_save = save_3
            print("\n" * 100)
            break
        elif save.lower() == "debug":
            chips.chosen_save = "debug"
            print("\n" * 100)
            break
        else:
            print("Please choose one of the three saves.")
            time.sleep(1.5)

    if chips.chosen_save == "debug":
        total = float("inf")
    else:
        try:
            with open(chips.chosen_save, "r") as file:
                total = int(float(file.read()))
        except FileNotFoundError:
            print("No save found, creating new save.")
            time.sleep(2)
            total = 100
        except Exception:
            print("Save not viable, creating new save.\n")
            time.sleep(2)
            total = 100


def take_bet(chips):

    while True:
        chips.bet = input(
            f"\nHow many chips out of {total} would you like to bet?\nType 'Back' to go back.\n"
        )

        if chips.bet.lower() in "back" and chips.chosen_save != "debug":
            choose_save(chips)
        else:
            try:
                chips.bet = int(chips.bet)
            except ValueError:
                print("Please put in a number, otherwise it wont work.")
            else:
                if chips.bet > total:
                    print("\n" * 100)
                    print(f"You only have {total} chips not {chips.bet} chips!")
                elif chips.bet == 0:
                    print("\n" * 100)
                    print("You have to bet something!")
                elif chips.bet < 0:
                    print("\n" * 100)
                    print(
                        "You can't bet less then nothing!\nThat makes no logical sense!"
                    )
                elif chips.bet < 10:
                    print("\n" * 100)
                    print("You have to bet more than that!")
                else:
                    break


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global game_on

    choice = input("\nHit or Stand? ").lower()
    if choice in "hit" and choice != "" and hand.value != 21:
        hit(deck, hand)
    elif hand.value == 21 and choice not in "hit":
        print("\nI'm not letting you bust yourself!")
        time.sleep(1.5)
        print("\n---- Player Stands. Dealers turn. ----")
        game_on = False
    else:
        print("\n---- Player Stands. Dealers turn. ----")
        game_on = False


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("you bust! 😡")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("you win! 😃")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("Dealer busts! 😃")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("Dealer wins! 😞")
    chips.lose_bet()


def push(player, dealer):
    print("\n" * 100)
    show_all(player, dealer)
    print("Dealer and Player tie! It's a push...")


def blackjack(player, dealer, chips, win=True):
    print("\n" * 100)
    show_all(player, dealer)
    if win:
        print("You got a blackjack! 😳")
        chips.win_bet(blackjack=True)
    else:
        print("The dealer got a blackjack! 😰")
        chips.lose_bet()


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


def play():
    choose_save(Chips)
    while True:
        # Print an opening statement
        print("\n" * 100)
        print("Hello and welcome to Blackjack.")
        print("A production by Ben & Son, a coding family.\n")
        global game_on
        game_on = True
        black_jack = False
        customising = False
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        player_hand.adjust_for_ace()

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        dealer_hand.adjust_for_ace()

        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100

        # Prompt the Player for their bet
        if player_chips.chosen_save == "debug":
            customising = True
            what_hand = ""
            forced_phand_value = player_hand.value
            forced_dhand_value = dealer_hand.value
            while customising:
                print("\n" * 100)
                if forced_phand_value == "":
                    forced_phand_value = player_hand.value
                if forced_dhand_value == "":
                    forced_dhand_value = dealer_hand.value
                modifications = input(
                    "Are there any modifications you would like to make to this game?\n\n1: Force Blackjack\n2: Set Player Hand Value\n3: Set Dealer Hand Value\nType 'Reset' to reset all changes.\nPress enter to exit.\n"
                )

                if modifications == "1":
                    print("\n" * 100)
                    what_hand = input(
                        "Which hand?\n\n1: Player Hand\n2: Dealer Hand\n3: Both\nPress enter to return.\n"
                    )
                    if what_hand == "1":
                        print("\n" * 100)
                        forced_phand_value = 21
                        print("Player hand now has a blackjack.")
                        time.sleep(2)
                    elif what_hand == "2":
                        print("\n" * 100)
                        forced_dhand_value = 21
                        print("Dealer hand now has a blackjack.")
                        time.sleep(2)
                    elif what_hand == "3":
                        print("\n" * 100)
                        forced_phand_value = 21
                        forced_dhand_value = 21
                        print("Both hands now have a blackjack.")
                        time.sleep(2)
                    else:
                        pass
                elif modifications == "2":
                    print("\n" * 100)
                    forced_phand_value = input(
                        "What should the player hand's value be?\nPress enter to return.\n"
                    )

                    if forced_phand_value != "":
                        print("\n" * 100)
                        print(f"The player hand's value is now {forced_phand_value}.")
                        time.sleep(2)
                elif modifications == "3":
                    print("\n" * 100)
                    forced_dhand_value = input(
                        "What should the dealer hand's value be?\nPress enter to return.\n"
                    )

                    if forced_dhand_value != "":
                        print("\n" * 100)
                        print(f"The dealer hand's value is now {forced_dhand_value}.")
                        time.sleep(2)
                elif modifications == "":
                    print("\n" * 100)
                    if (
                        forced_phand_value != player_hand.value
                        or forced_dhand_value != dealer_hand.value
                    ):
                        start = input(
                            f"Here is what things are now:\n\n  - Player Hand Value: {forced_phand_value}\n  - Dealer Hand Value: {forced_dhand_value}\n\nDo you wish to continue?\n"
                        ).lower()
                        if start in "yes":
                            player_hand.value = int(forced_phand_value)
                            dealer_hand.value = int(forced_dhand_value)
                            print("\n" * 100)
                            customising = False
                            break
                        else:
                            pass
                    else:
                        print("\n" * 100)
                        customising = False
                        break
                elif modifications.lower() in "reset":
                    print("\n" * 100)
                    forced_phand_value = player_hand.value
                    forced_dhand_value = dealer_hand.value
                    print("All changes have been reset.")
                    time.sleep(2)

        take_bet(player_chips)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        if player_hand.value == 21 and dealer_hand.value == 21:
            push(player_hand, dealer_hand)
            black_jack = True
        elif player_hand.value == 21:
            blackjack(player_hand, dealer_hand, player_chips)
            black_jack = True
        elif dealer_hand.value == 21:
            blackjack(player_hand, dealer_hand, player_chips, win=False)
            black_jack = True

        # PLAYERS TURN
        while game_on and not black_jack:

            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        # DEALERS TURN
        if player_hand.value <= 21 and not black_jack:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            # show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print("\nPlayer's chip total stands at", total)

        # Ask to play again
        if not replay():
            print("Thanks for playing!")
            time.sleep(1.5)
            print("\n" * 100)
            break


if __name__ == "__main__":
    play()
