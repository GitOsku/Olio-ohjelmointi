import random 

class Coin: 
    
    def __init__(self):
        self.sideup = 'Heads'
        self.valuutta = "Ruble"
        
    def toss(self):
        l = random.randint (0, 3)  
        if l == 0:
            self.sideup = 'Heads'
        elif l == 1:
            self.sideup = 'Tails'
        elif l == 2:
            self.sideup = 'Mihi se meni'
        else:
            self.sideup = 'Siihe jysähti pystyy'
    
    def currency(self):
        c = random.randint (0, 4)
        if c == 0:
            self.valuutta = 'Euro'
        elif c == 1:
            self.valuutta = 'Rupla'
        elif c == 2:
            self.valuutta = 'Pound'
        elif c == 3:
            self.valuutta = 'Dollar' 
        else: 
            self.valuutta = 'Yen'
        return self.valuutta
                
            
    def get_sideup(self):
        return self.sideup
        
        
    
def main():
    
    my_coin = Coin()
    
    print('This side is up:', my_coin.get_sideup())
    
    print('I am tossing the coin...')
    my_coin.toss()
    
    print('This side is up:', my_coin.get_sideup())
    
    print('The currency of the coin is: ', my_coin.currency())
    
    
    
main()