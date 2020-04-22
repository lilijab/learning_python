from random import shuffle


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{s} of {st}'.format(s=self.value, st=self.suit)


class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.cards = [(s, v) for s in suits for v in values]

    def __repr__(self):
        return 'Deck of {l} cards'.format(l=len(self.cards))

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        if len(self.cards) == 0:
            raise ValueError('There is no cards left in the deck')
        if num <= len(self.cards):
            return [self.cards.pop() for _ in range(num)]
        else:
            temp_cards = self.cards
            self.cards = []
            return temp_cards

    def deal_card(self):
        hand = self._deal(1)
        return hand[0]

    def deal_hand(self, num):
        hand = self._deal(num)
        return hand

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)