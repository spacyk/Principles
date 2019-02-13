from __future__ import print_function
from string import ascii_letters, digits
from math import sqrt
from itertools import *


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def create_list_of_cards(degree=7):
    """
    This function generates a list of character combinations using Finite Projective Geometries.
    Combinations in the list follow the rule of Dobble Card Game.
    Math behind the choice of numbers is explained in the link bellow.
    """
    if degree > 7:
        raise ValueError("Degree is too big, there is not enough ascii letters.")
    if not is_prime(degree):
        raise ValueError("Degree has to be prime number.")

    symbols = (ascii_letters + digits)[:degree * degree + degree + 1]

    master_card = symbols[:degree + 1]
    other_symbols = symbols[degree + 1:]
    symbol_groups = [other_symbols[i:i + degree] for i in range(0, len(other_symbols), degree)]

    final_cards = [master_card]
    final_cards.extend([master_card[0] + group for group in symbol_groups])

    for index_offset, master_symbol in enumerate(master_card[1:]):
        for first_position, _ in enumerate(symbol_groups):
            right_combination = "".join(
                [
                    group[
                        (first_position + group_index * index_offset) % len(symbol_groups)
                    ] for group_index, group in enumerate(symbol_groups)
                ]
            )
            final_cards.append(master_symbol + right_combination)

    print(final_cards)


def create_cards_other_solution(degree=7):
    """
    Nice, graphical solution. Taken from:
    https://stackoverflow.com/questions/6240113/what-are-the-mathematical-computational-principles-behind-this-game?fbclid=IwAR3WvkhgQqi-aSf1H6pJEuRi5d1T_sI7jI0Wupjo81ZDcPuPYnG7tRmYsBc
    """
    symbols = (ascii_letters + digits)[:degree * degree + degree + 1]

    cards, num_pictures = create_cards(degree)
    display_using_symbols(cards, num_pictures, symbols)
    check_cards(cards)


def create_cards(p=7):
    for min_factor in range(2, 1 + int(p ** 0.5)):
        if p % min_factor == 0:
            break
    else:
        min_factor = p
    cards = []
    for i in range(p):
        cards.append(set([i * p + j for j in range(p)] + [p * p]))
    for i in range(min_factor):
        for j in range(p):
            cards.append(set([k * p + (j + i * k) % p
                              for k in range(p)] + [p * p + 1 + i]))

    cards.append(set([p * p + i for i in range(min_factor + 1)]))
    return cards, p * p + p + 1


def display_using_symbols(cards, num_pictures, symbols):
    for pictures_for_card in cards:
        print("".join(symbols[picture] if picture in pictures_for_card else ' '
                      for picture in range(num_pictures)))


def check_cards(cards):
    for card, other_card in combinations(cards, 2):
        if len(card & other_card) != 1:
            print("Cards", sorted(card), "and", sorted(other_card),
                  "have intersection", sorted(card & other_card))


if __name__ == "__main__":

    create_list_of_cards(degree=7)

    create_cards_other_solution(degree=5)
