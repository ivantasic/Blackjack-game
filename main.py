import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hand():
    #my hand
    cards_dealad = random.sample(cards, 2)
    my_hand = cards_dealad[0] + cards_dealad[1]
    print(f"Your cards: {cards_dealad}, current score: {my_hand}")
    
    #computer hand
    dealers_cards = random.sample(cards, 2)
    dealer_hand = dealers_cards[0] + dealers_cards[1]
    print(f"Computer's first card is: {dealers_cards[0]}")
    
    # Does user wants to take more cards?
    go_on = True
    while go_on:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            new_card = random.sample(cards, 1)
            cards_dealad += new_card
            if sum(cards_dealad) > 21 and 11 in cards_dealad:
                index = cards_dealad.index(11)
                cards_dealad[index] = 1    
            print(f"Your new hand is: {cards_dealad} and total is: {sum(cards_dealad)}")
            if sum(cards_dealad) > 21:
                print("You lose.")
                return
    #player is done with drawing more cards 
        else:
            print(f"Your hand is: {cards_dealad} and total is: {sum(cards_dealad)}")
            # while dealer hands are less than 17 draw more cards
            while sum(dealers_cards) <= 17 and sum(dealers_cards) <= 21:
                new_card_dealer = random.sample(cards, 1)
                dealers_cards += new_card_dealer
                
                if sum(dealers_cards) > 21  and 11 in dealers_cards:
                    index = dealers_cards.index(11)
                    dealers_cards[index] = 1
                    
            print(f"Dealear's hand is: {dealers_cards}, and total is: {sum(dealers_cards)}")
            if sum(dealers_cards) > 21:
                print("You win!")
                return
            if sum(dealers_cards) < sum(cards_dealad):
                print("You win!")
                return
            if sum(dealers_cards) > sum(cards_dealad):
                print("You lose.")
            if sum(dealers_cards) == sum(cards_dealad):
                print(f"Your cards are: {cards_dealad}, dealer cards are: {dealers_cards}.\n It's a draw.")
            go_on = False
hand()