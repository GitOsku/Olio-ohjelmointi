import random

class Card: 
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show_card(self):
        print ("{} of {}".format(self.value, self.suit))
            
            
class Deck: 
    def __init__(self):
        self.cards = []
        self.build()
        
    def build (self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 2):
                self.cards.append(Card(s, v))
                
    def show_deck(self):
        for c in self.cards:
            c.show_card()
            
    def shuffle_deck(self):
        for i in range(len(self.cards)- 1, 0, - 1):
            r = random.randint(0, 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def draw_card(self):
        return self.cards.pop()
    

        
deck = Deck()
#deck.shuffle()



        

        