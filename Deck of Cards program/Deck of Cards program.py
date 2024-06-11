# Deck of Cards program
import random


class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit.upper()
        else:
            print("That's not a suit!")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number.upper()
        else:
            print("Please, enter a number from 2 till 10 or J,Q,K,A!")

    def is_picture_card(self):
        return self._number in ["J", "Q", "K", "A"]


class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print("Deck = " + str(self._cards))

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        # numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(s, n) for s in suits for n in numbers]

    def show(self):
        for cards in self._cards:
            cards.show()
        my_deck.show()

    def shuffle(self):
        for i in range(len(self._cards) - 1, 0, -1):
            r = random.randint(0, i)
            self._cards[i], self._cards[r] = self._cards[r], self._cards[i]
        print("Shuffled Deck = " + str(self._cards))

    def draw_card(self):
        return self._cards.pop()

    def is_card_present(self, card):
        return card in self._cards

    def deal(self, num_players, num_cards):
        if num_players * num_cards > len(self._cards):
            print("Not enough cards in the deck to deal.")
            return []

        hands = []
        for _ in range(num_players):
            hand = []
            for _ in range(num_cards):
                hand.append(self.draw_card())
            hands.append(hand)
        return hands


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show_hand(self):
        for card in self.cards:
            print(card)


my_deck = Deck()
my_deck.shuffle()

card = my_deck.draw_card()
print("Card Drawn: " + str(card))

# Check if a card is present in the deck
print("Is the card present in the deck?", my_deck.is_card_present(card))

# Deal cards to players
num_players = 4
num_cards_per_player = 5
hands = my_deck.deal(num_players, num_cards_per_player)
print("Hands dealt:")
for i, hand in enumerate(hands):
    print("Player", i+1, ":", hand)
