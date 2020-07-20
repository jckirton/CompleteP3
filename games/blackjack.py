"""
Creates and starts a playable and savable game of Blackjack.
"""
import random
import time

save_file = ".chips"
suits = ("❤️", "💎", "⚜️", "☘️")
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


# def save_game():
#     player_chips.save_chips()


class Chips:
    def __init__(self):
        try:
            with open(save_file, "r") as file:
                self.total = int(float(file.read()))
        except FileNotFoundError:
            print("No save found, creating new save.")
            self.total = 100
        except Exception:
            print("Save not viable.")
            self.total = 100
        self.bet = 0

    def save_chips(self):
        with open(save_file, "w") as file:
            file.write(str(self.total))

    def win_bet(self, blackjack=False):
        # self.total += self.bet if not blackjack else (self.bet * 1.5)
        if blackjack:
            self.total += self.bet * 1.5
        else:
            self.total += self.bet

        self.save_chips()

    def lose_bet(self):
        if (self.total - self.bet) == 0:
            print("\nYour Out of Chips!\nGiving new chip stack.")
            self.total = 100
            with open(save_file, "w") as file:
                file.write(str("100"))
        else:
            self.total -= self.bet
            self.save_chips()


def take_bet(chips):

    while True:
        try:
            chips.bet = int(
                input(f"How many chips out of {chips.total} would you like to bet? ")
            )
        except ValueError:
            print("please put in a number, otherwise it wont work.")
        else:
            if chips.bet > chips.total:
                print("\n" * 100)
                print(f"You only have {chips.total} chips not {chips.bet} chips!")
            elif chips.bet == 0:
                print("\n" * 100)
                print("You have to bet something!")
            elif chips.bet < 0:
                print("\n" * 100)
                print("You can't bet less then nothing!\nThat makes no logical sense!")
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
    elif hand.value == 21:
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
    print("you bust! 😡")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("you win! 😃")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts! 😃")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins! 😞")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push...")


def blackjack(player, chips):
    print("You got a blackjack! 😳 ")
    chips.win_bet(blackjack=True)


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
    while True:
        # Print an opening statement
        print("\n" * 100)
        print("Hello and welcome to Blackjack.")
        print("A production by Ben & Son, a coding family.")
        global game_on
        game_on = True
        black_jack = False
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100

        # Prompt the Player for their bet
        take_bet(player_chips)
        # player_hand.value = 21
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        if player_hand.value == 21:
            blackjack(player_hand, player_chips)
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
        print("\nPlayer's chip total stands at", player_chips.total)

        # Ask to play again
        if not replay():
            print("Thanks for playing!")
            time.sleep(1.5)
            print("\n" * 100)
            break


if __name__ == "__main__":
    play()
