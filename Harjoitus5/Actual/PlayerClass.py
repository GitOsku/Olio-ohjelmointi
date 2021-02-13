from Dicefilu import Dice

class Player(Dice): 
    
    def __init__(self, id):
        self.firstname = "Oskari"
        self.lastname = "Helenius"
        self.ID = id
        self.roll = 0
    
    #setters
    
    def setFirstname(self):
        set_firstname = input("Gimme your firstname: ")
        self.firstname = set_firstname
        
    
    def setlastname(self):
        set_lastname = input("Gimme your lastname: ")
        self.lastname = set_lastname 
        
        
    def setIdenticator(self, ID):
        self.ID = ID
        
    #getters
    
    def getFirstname(self):
        return self.firstname
    
    def getLastname(self):
        return self.lastname
    
    def getIdenticator(self):
        return self.ID
    
    def __str__(self):
        return "\nFirsname: " + format(self.firstname)\
            + "\nLastname: " + format(self.lastname)\
            + "\nID: " + format(self.ID)
            
            
def main():
    
    Player1 = Player(1)
    Player1.set_toss() #rolling dice
    
    Player2 = Player(2)
    Player2.set_toss() #rolling dice
    
    Player3 = Player(3)
    Player3.set_toss() #rolling dice
    
    
    dicti = {
        Player1.getIdenticator(): Player1.get_toss(),
        Player2.getIdenticator(): Player2.get_toss(),
        Player3.getIdenticator(): Player3.get_toss()
        }
    
    for key, value in dicti.items():
        print("Player", key, ' rolled: ', value)

    
main()    