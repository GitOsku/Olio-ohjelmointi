import random 



class Dice:
    
   # def __init__(self):
    #    self.roll ='1'

    def toss(self):
        
        self.roll = random.randint (1, 6)
        return self.roll
    
def main():
    
    dices = []
    
    for i in range(0, 3):
        dices.append(Dice())
        
    
    while True:
        results = []
        for i in range(0, 3):
            dices[i].toss()
            results.append(dices[i].roll)
            i += 1
        print("First player: ", results[0])
        print("Second player: ", results[1])
        print("Third player: ", results[2])
        
        if (max(results) > dices[1].roll and max(results) > dices[2].roll) or (max(results) > dices[0].roll and max(results) > dices[1].roll) or (max(results) > dices[0].roll and max(results) > dices[2].roll):
            print ("Now checking winner")
            print("Winner is", results.index(max(results))+1)
            dices.remove(max(results))
            for dice in dices:
                dice.toss()
            if dices[0] > dices[1]:
                print("Player 1 wins")
            else:
                print("Player 2 wins")
        elif dices[0].roll != dices[1].roll and dices[0].roll != dices[2].roll and dices[1].roll != dices[2].roll:
            return

main()