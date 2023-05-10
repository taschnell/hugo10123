
_possible_ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
_possible_suits = ["♥","♠","♦","♣"]

possible_cards = []

from itertools import permutations

for suit in _possible_suits:
    for rank in _possible_ranks:
        possible_cards.append(suit+rank)

possible_hand = permutations(possible_cards, 5)

for i in possible_hand:
    print(i)