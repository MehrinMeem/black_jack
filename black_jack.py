import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    score = sum(card_list)

    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)

    return score


print("Blackjack game started")