from Deck_of_Cards import Deck
from Deck_of_Cards import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = 0

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


class Game:
    def __init__(self, player_name_1, player_name_2, num_play_round: int = float('inf'), num_of_winner: int = 1):
        self.num_play_round = num_play_round
        self.num_of_winner = num_of_winner
        self.deck = Deck()
        self.player_1 = Player(player_name_1)
        self.player_2 = Player(player_name_2)
        self.num_play_round = num_play_round
        self.current_number_of_runs = 0

    def initialize_game(self):
        self.deck.shuffle()
        half_a_deck = len(self.deck.deck) // 2
        self.player_1.hand = self.deck.deal_hand(half_a_deck)
        self.player_2.hand = self.deck.deal_hand(half_a_deck)

    def creating_a_stack(self, stack: list = [], num_card: int = 1):
        """Adds to the list (or create a list and adds) N cards from each player"""
        for i in range(num_card):
            stack.append(self.player_1.hand.pop(0))
            stack.append(self.player_2.hand.pop(0))
        return stack

    def play_round(self, ls: list):
        if ls[-2] < ls[-1]:
            self.taking_loot(ls, self.player_2)
        if ls[-2] > ls[-1]:
            self.taking_loot(ls, self.player_1)
        if ls[-2] == ls[-1]:
            self.tie_wer(ls)

    def taking_loot(self, ls_card: list, winner):
        winner.hand.extend(ls_card)

    def tie_wer(self, ls: list):
        print('ווואאוווו מלחמה')
        minimum = min(len(self.player_1.hand), len(self.player_1.hand))
        if minimum:
            stock = self.creating_a_stack(ls, min(3, minimum))
            self.play_round(stock)
        else:
            self.the_winner()

    def the_winner(self):
        if len(self.player_1.hand) < len(self.player_2.hand):
            print(self.player_2.name)
        if len(self.player_1.hand) > len(self.player_2.hand):
            print(self.player_1.name)
        if len(self.player_1.hand) == len(self.player_2.hand):
            print('tie')

    def main(self):
        self.initialize_game()
        while 0 < len(self.player_1.hand) < 52 and self.current_number_of_runs < self.num_play_round:
            self.play_round(self.creating_a_stack())
            self.current_number_of_runs += 1
        self.the_winner()


a = Game('shneor', 'zalman')


a.main()
