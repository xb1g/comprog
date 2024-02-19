import math

circle_area = lambda r: math.pi * r ** 2

print(circle_area(5))

count_vowel = lambda s: sum([1 for c in s if c in 'aeiouAEIOU'])

print(count_vowel('hello broski'))
print(count_vowel('AAAA'))

print_deck = lambda: [print(f'{r} of {s}') for s in '♠♥♦♣' for r in range(1,14)]

print_deck()

class playing_card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

card = playing_card(12, '♥')
print(card)
deck_cards = [playing_card(r,s) for s in '♠♥♦♣' for r in range(1,14)]

print(deck_cards)