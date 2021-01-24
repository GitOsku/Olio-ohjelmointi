import random 

class Coin: 
    
    def __init__(self):
        self.sideup = 'Heads'
        
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
    
            
            
            
    def get_sideup(self):
        return self.sideup
        
        
    
def main():
    
    my_coin = Coin()
    
    print('This side is up:', my_coin.get_sideup())
    
    print('I am tossing the coin...')
    my_coin.toss()
    
    print('This side is up:', my_coin.get_sideup())
    
    
main()