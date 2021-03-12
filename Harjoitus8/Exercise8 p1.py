import random

class House: 
        
    def __init__(self, windows, floors, bed, surfaces, fridge, toiletpaper):
        self.windows = windows
        self.floors = floors
        self.bed = bed
        self.surfaces = surfaces 
        self.fridge = fridge
        self.toiletpaper = toiletpaper

        #setters
        
    def setWindows(self, windows):
        self.windows = windows
        
    def setFloors(self, floors):
        self.floors = floors
        
    def setBed(self, bed):
        self.bed = bed 
        
    def setSurfaces(self, surfaces):
        self.surfaces = surfaces
        
    def setFridge(self, fridge):
        self.fridge = fridge
        
    def setToiletpaper(self, toiletpaper):
        self.toiletpaper = toiletpaper
      

    #getters
    
    def getWindows(self):
            return self.windows
        
    def getFloors(self):
            return self.floors
        
    def getBed(self):
            return self.bed
        
    def getSurfaces(self):
            return self.surfaces
        
    def getFridge(self):
            return self.fridge
        
    def getToiletpaper(self):
            return self.toiletpaper
        
    #setters
    
    def __str__(self):
       return "\nWindows are " + format(self.windows)\
            + "\nFloors are " +format(self.floors)\
            + "\nBed is " + format(self.bed)\
            + "\nSurfaces are " + format(self.surfaces)\
            + "\nFridge is " + format(self.fridge)\
            + "\nToiletpaper is " + format(self.toiletpaper)\
               
        
class Cookie:
    
    def __init__(self, init_shape):
        self.shape = init_shape
        
    #setters    
     
    
    def setShape(self, desired_shape):
        self.shape = desired_shape
        
    def setFlavor(self):
        flavorlist = ["Chocolate", "Vanilla", "Doublechocolate", "Nut", "Strawberry", "Lemon", "Rasberry", "Whitechocolate", "Toffee", "MM's", "Liquorice" ]
        self.flavor = random.choice(flavorlist)
          
    #getters
    
    def getSHape(self):
        return self.shape 
    
    def getFlavor(self):
        return self.flavor
    

    
    #str-method    
    
    def __str__(self):
       return "\nShape of cookie: " + format(self.shape)\
           + "\nFlavor of cookie: " +format(self.flavor)\
       

            
                    
def main():
    
    #State 1
    
    house = House("dirty", "dirty", "unmade", "dusty", "empty", "running out", )
    print(house)
    
    #State 2
    
    house.setWindows("washed")
    house.setBed("made")
    print(house)
    
    #State 3
    
    house.setFloors("vacuumed")
    house.setSurfaces("dusted")
    print(house)
    
    #State 4
    
    house.setFridge("full")
    house.setToiletpaper("enough")
    print(house)
    
    #State 5
    
    house.setToiletpaper("more than enough")
    print(house)
    
    favoriteflavor = "Chocolate"
    
    Favoriteflavor = input("Gimme flavor! ")
    
    mainlist = []
    for i in range(10):
        cookie = Cookie("round")
        mainlist.append(cookie)
    
    for key in mainlist:
        key.setFlavor()
        if key.getFlavor() == Favoriteflavor:
            print("this was your favorite flavor! ")
        else:
            print("was not")
        
        
    
main()   

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    