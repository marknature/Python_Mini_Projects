# Deck of Cards

## Introduction

The "Deck of Cards" project aims to create a reusable object-oriented model of a deck of cards in Python. This model can serve as the foundation for building digital card game programs, such as Poker or Gin Rummy.

## Object-Oriented Programming (OOP)

Object-oriented programming (OOP) is a way of organizing your code to make it easier to understand, reuse, and modify. In OOP, you combine data (variables) and functionality, wrapping them together inside objects.

## Implementation

### Card Class

The `Card` class represents an individual playing card. It has the following attributes and methods:

- `suit`: The suit of the card (e.g., hearts, clubs, diamonds, spades).
- `number`: The number or face value of the card (e.g., 2, 3, 4, ..., 10, J, Q, K, A).
- `is_picture_card()`: Determines whether the card is a picture card (J, Q, K, A).

### Deck Class

The `Deck` class represents a deck of cards. It includes the following methods:

- `populate()`: Creates a standard deck of 52 cards.
- `shuffle()`: Shuffles the deck.
- `draw_card()`: Draws a card from the deck.
- `is_card_present(card)`: Checks if a specific card is present in the deck.
- `deal(num_players, num_cards)`: Deals cards to players.

### Example Usage

```python
# Create a deck
my_deck = Deck()

# Shuffle the deck
my_deck.shuffle()

# Draw a card
card = my_deck.draw_card()
print("Card Drawn:", card)

# Check if a card is present in the deck
print("Is the card present in the deck?", my_deck.is_card_present(card))

# Deal cards to players
num_players = 4
num_cards_per_player = 5
hands = my_deck.deal(num_players, num_cards_per_player)
print("Hands dealt:")
for i, hand in enumerate(hands):
    print("Player", i + 1, ":", hand)
```


Published by Raspberry Pi Foundation (https://www.raspberrypi.org) under a Creative Commons
license (https://creativecommons.org/licenses/by-sa/4.0/).

View project & license on GitHub (https://github.com/RaspberryPiLearning/deck-of-cards)
