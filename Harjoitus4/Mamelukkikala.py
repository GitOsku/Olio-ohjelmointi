from Dicefilu import Dice

from Carfilebruum import Car


class Mammal:
    
    def __init__(self, id, specie, name, size, weight, height, width):
        self.ID = id
        self.specie = specie 
        self.name = name
        self.size = size
        self.weight = weight
        self.height = height
        self.width = width
        
        
    def __str__(self):
        return "Maker: " + format(self.ID)\
                + "\nModel: " + format(self.specie)\
                + "\nMileage: " + format(self.name)\
                + "\nPrice: " + format(self.size)\
                + "\nColor: " + format(self.weight)\
                + "\nMaximum: " + format(self.height)\
                + "\nTrunk: " + format(self.width)\

        
        
def main():
    
    my_dice = Dice()
    
    #for example the fishes 2 is kgs and the last ones are centtimeters
    
    my_mammal = Mammal(1, "Fish", "John" ,"massive", 2, 40, 30)
    my2_mammal = Mammal(2, "Squirel", "Jyrsis", "small", 0.4, 20, 10)
    my3_mammal = Mammal(3, "Cat", "Sack", "big", 5, 60, 40)
    my4_mammal = Mammal(4, "Hamster", "Pasi", "small", 0.04, 5, 5)
    my5_mammal = Mammal(5, "Rabbit", "Tero", "Mid-size", 0.5, 30, 20)
    my6_mammal = Mammal(6, "Elephant", "Dumbo", "Very big", 7500, 5000, 2500)
    
    
    
   # result = my_dice.toss()
    
    if my_dice.roll == 1:
        print (my_mammal)
        
    elif my_dice.roll == 2:
        print (my2_mammal)
    
    elif my_dice.roll == 3:
        print (my3_mammal)
        
    elif my_dice.roll == 4:
        print (my4_mammal)
        
    elif my_dice.roll == 5:
        print (my5_mammal)
        
    else:
        print (my6_mammal)

        
    print(my_mammal.__str__())
    
          
main()
    
    
        
        

