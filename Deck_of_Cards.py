import random


class Card:
    def __init__(self, rank=None, suit=None, name=None):
        self.rank = rank
        self.suit = suit
        self.name = name

    def __str__(self):
        return f'({self.name}, {self.suit})'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        return self.rank > other.rank


a = Card(1, 'k')
b = Card(1, 'k')


class Deck:

    def __init__(self, joker=0):
        self.deck = []
        four_suits = ['Spade', 'Heart', 'Diamond', 'Club']
        names_and_rank = [('a', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
                          ('8', 8), ('9', 9), ('10', 10), ('J', 11), ('q', 12), ('k', 13)]
        for suit in four_suits:
            for j in names_and_rank:
                name, rank = j
                self.deck.append(Card(rank, suit, name))
        for i in range(joker):
            self.deck.append(Card(14, None, 'Joker'))

    def sort_by_rank(self):
        self.deck = sorted(self.deck, key=lambda x: x.rank)

    def sort_by_suit(self):
        self.deck = sorted(self.deck, key=lambda x: x.suit)

    def shuffle(self):
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, x):
        return self.deck[x]

    def draw(self):
        return self.deck.pop()

    def deal_hand(self, num_cards: int):
        if num_cards > len(self.deck):
            return False
        hand = []
        for i in range(num_cards):
            first_card = self.deck.pop()
            hand.append(first_card)
        return hand

    def count_cards(self, rank):
        count_cards = 0
        for card in self.deck:
            if card.rank == rank:
                count_cards += 1
        return count_cards



