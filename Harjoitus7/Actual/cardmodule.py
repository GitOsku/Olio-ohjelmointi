import random

class Card: 
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show_card(self):
        print ("{} of {}".format(self.value, self.suit))
        