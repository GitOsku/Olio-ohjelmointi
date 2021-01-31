import random 
 
class Dice:
    
    def __init__(self):
        self.roll ='1'
        self.color = 'black'
        self.form = 'Cube'
        
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
    
    def vari(self): #nopan väri
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
    
    def shape(self): #Nopan muoto
        m = random.randint(0, 3)
        if m == 0:
            self.form = 'Cube'
        if m == 1:
            self.form = 'Pyramid'
        if m == 2:
            self.form = 'Tetraedri'
        else: 
            self.form = 'Hexagon'
        return self.form
    
    
def main():
    
    my_dice = Dice()
    my2_dice = Dice()
    
    print('Your fortune number is: ', my_dice.toss())
    
    print("Your dice's color is: ", my_dice.vari())
    
    print('Your second dices toss is: ', my2_dice.toss())
          
    print("The sum of the dices are: ", int(my_dice.roll) + int(my2_dice.roll))
    
    print("Your dice's shape is: ", my_dice.shape())
          
main()