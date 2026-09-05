import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    score = sum(card_list)

    if score == 21 and len(card_list) == 2:
        return 0

    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"

    elif computer_score == 0:
        return "Computer has Blackjack. You lose."

    elif user_score == 0:
        return "You have Blackjack. You win!"

    elif user_score > 21:
        return "You went over 21. You lose."

    elif computer_score > 21:
        return "Computer went over 21. You win!"

    elif user_score > computer_score:
        return "You win!"

    else:
        return "You lose."


user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

game_over = False

while not game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("Your cards:", user_cards)
    print("Your score:", user_score)
    print("Computer first card:", computer_cards[0])

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        choice = input("Type 'y' to get another card, or 'n' to pass: ")

        if choice == "y":
            user_cards.append(deal_card())
        else:
            game_over = True


while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


print("Your final cards:", user_cards)
print("Your final score:", user_score)

print("Computer final cards:", computer_cards)
print("Computer final score:", computer_score)

print(compare(user_score, computer_score))