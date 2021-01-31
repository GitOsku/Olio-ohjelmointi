import random 

class Coin: 
    
    def __init__(self):
        self.__sideup = 'Heads'
        self.valuutta = 'Ruble'
        self.question = input("GIMME MY MONEY BITCH: ")
        
    def toss(self):
        l = random.randint (0, 3)  
        if l == 0:
            self.__sideup = 'Heads'
        elif l == 1:
            self.__sideup = 'Tails'
        elif l == 2:
            self.__sideup = 'Mihi se meni'
        else:
            self.__sideup = 'Siihe jysähti pystyy'
    
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
    
    def chosen_one(self):
        if self.question == 'Euro' :
            self.valuutta = 'Euro'  
        if self.question == 'Rupla' :
            self.valuutta = 'Rupla'
        if self.question == 'Pound' :
            self.valuutta = 'Pound'
        if self.question == 'Dollar' :
            self.valuutta = 'Dollar' 
        if self.question == 'Yen' : 
            self.valuutta = 'Yen'
        return self.valuutta
        
                
            
    def get_sideup(self):
        return self.__sideup
        
        
    
def main():
    
    my_coin = Coin()
    
    print('This side is up:', my_coin.get_sideup())
    
    print('I am tossing the coin...')
    my_coin.toss()
    
    print('This side is up:', my_coin.get_sideup())
    
    print('The random currency of the coin is: ', my_coin.currency())
    
    print("The currency you wanted: ", my_coin.chosen_one())
    
    
main()