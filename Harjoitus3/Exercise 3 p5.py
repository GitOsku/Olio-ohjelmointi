import random 

class Dice: 
    
    def __init__(self):
        self.roll ='1'
        self.color = 'black'
        
    def toss(self):
        
        l = random.randint (0, 5)
        if l == 0:
            self.roll = '1'
        elif l == 1:
            self.roll = '2'
        elif l == 2:
            self.roll = '3'
        elif l == 3:
            self.roll = '4'
        elif l == 4:
            self.roll = '5'
        else:
            self.roll = '6'
        
        return self.roll
    
    def vari(self): 
        k = random.randint(0, 3)
        if k == 0:
            self.color = 'Black'
        elif k == 1: 
            self.color = 'White'
        elif k == 2:
            self.color = 'Red'
        else:
            self.color = 'Green'
        return self.color
        
    
    
def main():
    
    my_dice = Dice()
    
    print('Your fortune number is: ', my_dice.toss())
    
    print("Your dice's color is: ", my_dice.vari())
    
main()