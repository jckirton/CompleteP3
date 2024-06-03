"""
A playable game of Blackjack, with saves.
Also my first proper use of object oriented programming.
"""

import random
import time

# Defining global variables. These are:
# Save file names, the player's chip total, card suits, card ranks and their corrosponding integer values, and the player turn state.
save_1 = ".chips"
save_2 = ".chips2"
save_3 = ".chips3"
total = 0
# Unicode characters for the suits. Suits looks like: (♥, ♦, ♠, ♣)
suits = ("\u2665", "\u2666", "\u2660", "\u2663")
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
player_turn = True


# Defining the card object.
class Card:
    """
    A card, with the components suit and rank.

    suit: The card's suit.
    rank: The card's rank.
    """

    def __init__(self, suit: str, rank: str):
        # The actual card.
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # String representation of the card. If you try to print it or make it a string, this is what you get.
        return f"{self.rank} of {self.suit}"


# Defining the deck object.
class Deck:
    """
    A standard deck of 52 cards.
    Shuffling and dealing included.
    Correct order not included, that's up to you.
    """

    def __init__(self):
        # Making the actual deck. Done by making a card of every rank for every suit.
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        # String representation of the deck.
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return f"The deck has:{deck_comp}"

    def shuffle(self) -> None:
        """
        It's a deck. You shuffle it. I could not be clearer about what this is.
        """
        random.shuffle(self.deck)

    def deal(self) -> Card:
        """
        Returns the top card of the deck.

        You could call this drawing, but this is blackjack. You don't draw, you deal or get dealt to.
        """
        return self.deck.pop(0)


# Defining hand object.
class Hand:
    """
    A hand of cards. Has the cards it's holding, the value of the hand, and the number of aces in the hand.

    You can add cards to it, and have it adjust the value for aces.
    """

    def __init__(self):
        # Making the hand. Initially, it holds nothing.
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        """
        Adds the given card to the hand, and adjusts the hand's value and ace count accordingly.

        card: The card being added to the hand.
        """

        def adjust_for_ace(self):
            """
            Adjusts the hand value to account for aces, because aces are funky in blackjack.
            """
            # Checking if the hand value is greater than 21, and there are aces worth 11 present.
            # This is the criteria for an ace changing value from 11 to 1.
            while self.value > 21 and self.aces:
                # Adjuting the hand value.
                self.value -= 10
                # Adjusting the count of "11-aces".
                self.aces -= 1

        # Adding the card to the hand.
        self.cards.append(card)
        # Adjusting the hand value.
        self.value += values[card.rank]
        # Checking if it's an ace, and counting it if so.
        if card.rank == "Ace":
            self.aces += 1

        adjust_for_ace(self)


# Defining the chips object.
class Chips:
    """
    The player's chips. Not for eating.

    Handles the result of winning and losing bets, and saving.
    """

    # The chosen save, so it knows which save it's dealing with. Starts off unchosen.
    chosen_save = ""

    def __init__(self):
        # Making the chips. The player's chip total is not defined here as that is a global variable.
        self.bet = 0

    def save_chips(self):
        """
        Saves the player's chips to the chosen save.
        """
        # Stating that we're referencing the global total variable.
        global total

        # Saving the game if the chosen save is not the debug "save".
        if self.chosen_save != "debug":
            # Rounding the player's chip value, as winning from a blackjack often results in a float.
            total = round(total)
            # Writing the new state to the chosen save.
            with open(self.chosen_save, "w") as file:
                file.write(str(total))

    def win_bet(self, blackjack=False):
        """
        Calculates the player's winnings, and saves the game.

        blackjack: Adjusts the winnings calculation for a blackjack if True. False by default.
        """
        # Referencing the global total variable.
        global total

        # Adjusts the winnings calculation if there's a blackjack, and the chosen save isn't debug.
        if blackjack and self.chosen_save != "debug":
            # The adjusted calculation.
            total += self.bet * 1.5
            # Rounding to an int.
            total = round(total)
        else:
            # Standard winnings calculation.
            total += self.bet

        # Saving the game.
        self.save_chips()

    def lose_bet(self):
        """
        Calculates the player's losses, gives the player a new chipstack if needed, and saves the game.
        """

        # Referencing the global total varible.
        global total
        # Variable for fancy thing for changing the text between "chip" and "chips" depending on the number of chips.
        mto = ""

        # The fancy thing.
        if (total - self.bet) > 1:
            mto = "s"
        # Gives the player a new chipstack if they've run out of chips, and saves.
        if (total - self.bet) == 0:
            print("\nYour Out of Chips!\nGiving new chipstack.")
            total = 100
            self.save_chips()
        # Same as above, but for if they have less than 10 chips left.
        elif (total - self.bet) < 10:
            print(
                f"\n{total - self.bet} chip{mto} is not enough to continue!\nHere, have a new chipstack."
            )
            total = 100
            self.save_chips()
        # Standard loss calculation and saving.
        else:
            total -= self.bet
            self.save_chips()


# Defining game functions.
def choose_save(chips: Chips):
    """
    Displays the saves and prompts the user to choose a save, and updates the player's chip total accordingly.
    Also handles the creation of a new save if the chosen save wither doesn't exist, or is invalid.

    chips: The chips object instance.
    """

    # Referencing the global total variable.
    global total

    # Reading the saves so they may be displayed.
    # Uses try-except blocks to handle the save being invalid or nonexistant.
    try:
        # Trying to open and read the save file.
        # If the file doesn't exist, a FileNotFoundError is thrown.
        with open(save_1, "r") as file:
            # Converting the save file from a string, to a number to check for validity, and then back to a string for displaying.
            # If the save is invalid, a ValueError is thrown.
            save1_total = str(int(float(file.read()))) + " Chips"
    except FileNotFoundError:
        save1_total = "No Save"
    except ValueError:
        save1_total = "Save Invalid"

    # Identical to the above, but with save 2 and 3 respectively.
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

    # Prompting the user to choose a save. Contained within a loop to redo the prompt upon an invalid answer.
    while True:
        # "Clearing" the terminal for the prompt.
        print("\n" * 100)
        # The prompt.
        save = input(
            f"Which save would you like to use?\n1: {save1_total}\n2: {save2_total}\n3: {save3_total}\n\n"
        )

        # Setting the chosen save.
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
        # Reprompting the user upon an invalid input.
        else:
            print("Please choose one of the three saves.")
            time.sleep(1.5)

    # Updating the total variable based on the chosen save.
    if chips.chosen_save == "debug":
        # If the chosen save is "debug", total is set to infinity.
        total = float("inf")
    else:
        # Reading and converting the file to a number, then setting total to the result.
        # Contained within a try-except block to catch errors from missing or invalid save files, and handle them accordingly.
        try:
            # Attempting to open the chosen save file.
            # If the chosen save file is missing, a FileNotFoundError is thrown.
            with open(chips.chosen_save, "r") as file:
                # Converting the file contents to a number, and updating the global total variable.
                # If the save file is invalid, a ValueError is thrown.
                total = int(float(file.read()))
        # Catches a FileNotFoundError and handles it accordingly.
        except FileNotFoundError:
            # New file creation dialog.
            print("No save found, creating new save.")
            time.sleep(2)
            # Setting the total variable to the value of a new save; 100.
            total = 100
        # Catches any other error and handles it accordingly.
        except Exception:
            # New file creation dialog.
            print("Save not viable, creating new save.\n")
            time.sleep(2)
            # Setting the total variable to the value of a new save; 100.
            total = 100


def take_bet(chips: Chips):
    """
    Prompts the user for their bet, or lets them change their save.

    chips: The player chips instance.
    """

    # Contained within a loop for reprompting after an invalid input, or the chosen save being changed.
    while True:
        # Prompt and input.
        chips.bet = input(
            f'\nHow many chips out of {total} would you like to bet?\nType "Back" to go back.\n\n'
        )

        # Checking if the user decided to go back.
        # Going back is disallowed if the debug save was chosen due to the debug menu allowing you to "rig" games.
        if chips.bet.lower() in "back" and chips.chosen_save != "debug":
            choose_save(chips)
        # Handling the user's bet input.
        else:
            # Contained within a try-except block to catch errors and stuff.
            try:
                # Converting the input to an int and storing that.
                # If the input is invalid, a ValueError is thrown.
                chips.bet = int(chips.bet)
            # ValueError handling.
            except ValueError:
                # Prompting the user to enter a number, then requesting the bet again.
                print("Please put in a number, otherwise it wont work.")
            else:
                # Checking if the bet made was too big, too little, or negative, and giving funny dialog.
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
                # The bet was valid. Exiting the loop.
                else:
                    break


def hit(deck, hand):
    """
    The hit action. Deals a card to the given hand.

    deck: The deck object.
    hand: The hand that's hitting.
    """
    # Gets the top card, gives it to the hand, and tells the hand to do ace math.
    card = deck.deal()
    hand.add_card(card)


def hit_or_stand(deck: Deck, player_hand: Hand):
    """
    Asks the player what they would like to do for their turn.

    deck: The deck object.
    hand: The player hand.
    """
    # Referencing the global player turn variable.
    global player_turn

    # Getting the player's choice of action.
    choice = input("\nHit or Stand?\n").lower()
    # If the player types hit or something adjacent to it that isn't nothing, hit.
    # If they input nothing, they stand.
    if choice in "hit" and choice != "" and player_hand.value != 21:
        hit(deck, player_hand)
    # Stoping the player from ruining a perfect hand, and making them stand.
    elif player_hand.value == 21 and choice in "hit" and choice != "":
        print("\nI'm not letting you bust yourself!")
        time.sleep(1.5)
        print("\n---- Player Stands. Dealers turn. ----")
        player_turn = False
    # The player stands.
    else:
        print("\n---- Player Stands. Dealers turn. ----")
        player_turn = False


def show_some(player: Hand, dealer: Hand):
    """
    Shows the player and dealer hands. But only some of the dealer's.

    player: The player hand.
    dealer: The dealer hand.
    """
    # Showing the hands. Funky string stuff.
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


def show_all(player: Hand, dealer: Hand):
    """Shows the player and dealer hands. All of it this time.

    player: The player hand.
    dealer: The dealer hand.
    """
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


# Functions run upon the according game end condition.
# Shows hands, prints some text, and tells the chips object to do the appropriate thing.


# Player-caused winn and loss conditions.
def player_busts(player: Hand, dealer: Hand, chips: Chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("You bust!")
    chips.lose_bet()


def player_wins(player: Hand, dealer: Hand, chips: Chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("You win!")
    chips.win_bet()


# Dealer caused win and loss conditions.
def dealer_busts(player: Hand, dealer: Hand, chips: Chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player: Hand, dealer: Hand, chips: Chips):
    print("\n" * 100)
    show_all(player, dealer)
    print("Dealer wins!")
    chips.lose_bet()


# A tie.
def push(player: Hand, dealer: Hand):
    print("\n" * 100)
    show_all(player, dealer)
    print("Dealer and Player tie! It's a push...")


# A blackjack occurs.
# Basically the same, but it can happen to both the player and the dealer, and it does blackjack math for winnings.
def blackjack(player: Hand, dealer: Hand, chips: Chips, win=True):
    """
    A blackjack happened.

    win: Weather or not the player is the one who won. True by default.
    """
    print("\n" * 100)
    show_all(player, dealer)
    if win:
        print("You got a blackjack!")
        chips.win_bet(blackjack=True)
    else:
        print("The dealer got a blackjack!")
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
    """
    The actual gameplay loop.
    """
    # Initial save choice.
    choose_save(Chips)
    while True:
        # Welcome screen.
        print("\n" * 100)
        print("Hello and welcome to Blackjack.")
        print("A production by Ben & Son, a coding family.\n")
        global player_turn
        player_turn = True
        black_jack = False
        customising = False

        # Create & shuffle the deck, deal two cards to each player.
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips.
        player_chips = Chips()

        # The debug menu. You don't need to pay too much attention to this.
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

        # Taking player bet.
        take_bet(player_chips)
        # Show cards, but keep one dealer card hidden
        show_some(player_hand, dealer_hand)

        # Checking for blackjack conditions.
        if player_hand.value == 21 and dealer_hand.value == 21:
            push(player_hand, dealer_hand)
            black_jack = True
        elif player_hand.value == 21:
            blackjack(player_hand, dealer_hand, player_chips)
            black_jack = True
        # elif dealer_hand.value == 21:
        #     blackjack(player_hand, dealer_hand, player_chips, win=False)
        #     black_jack = True

        # Player turn.
        while player_turn and not black_jack:

            # Prompt for player action.
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # Check for player bust condition (when hand value > 21), and end game if so.
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        # Dealer turn.
        if player_hand.value <= 21 and not black_jack:

            # Dealer takes cards until their hand value is ≥ 17.
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Check for game end scenarios.
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print(f"\nPlayer's chip total stands at {total}")

        # Ask to play again
        if not replay():
            print("Thanks for playing!")
            time.sleep(1.5)
            print("\n" * 100)
            break


# Fancy thing for running the game if the blackjack file itself is being run.
# Also avoids the play function being run upon an import of the file.
if __name__ == "__main__":
    play()
