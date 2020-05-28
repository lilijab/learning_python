import unittest
from deck_of_cards import Card
from deck_of_cards import Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card('Hearts', 'A')

    def test_init(self):
        self.assertEqual(self.card.suit, 'Hearts')
        self.assertEqual(self.card.value, 'A')

    def test_repr(self):
        self.assertEqual(repr(self.card), 'A of Hearts')


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_repr(self):
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)

    def test_deal_enough_cards(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_not_enough_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_error(self):
        self.deck.deal_hand(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_hand(self):
        cards = self.deck.deal_hand(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_shuffle_full(self):
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full(self):
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

