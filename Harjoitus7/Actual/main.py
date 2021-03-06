# File:         main.py
# Author:       
# Description:  Deck of cards and card games.



from cardmodule import Card
from deckmodule import Deck

def main():
    
    print("Let's test that a single card works...")
    
    my_card = Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    
    
    
    # Code your Exercise 7 taks 4 game here. 
    #line breakers 
    
    print("")
    print("")
    cardlist = []
      
    print("The first card is: ")
    card1 = my_deck.draw_card()
    card1.show_card()
    cardlist.append(card1.value)
    
    print("The second card is: ")
    card2 = my_deck.draw_card()
    card2.show_card()
    cardlist.append(card2.value)
    
    print("The third card is: ")
    card3 = my_deck.draw_card()
    card3.show_card()
    cardlist.append(card3.value)
    
    cardlist.sort()

    if ((cardlist[0] == cardlist[1]) or (cardlist[1] == cardlist[2])):
        print("\nIt's a draw")
        
    else: 
        
        print("\nThe biggest number is:")
        print(cardlist [-1])

    
    
    
    
    

# Calling the main function here, do not change...
main()
