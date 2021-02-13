from Mammal import Mammal

class Student():
    
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.ID = id
        

        
    #setters
        
    def setFirstname(self, firstname):
            self.firstname = firstname
            
            
    def setLastname(self, lastname):
            self.lastname = lastname
            
        
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
    
    student1 = Student("Oskari", "Helenius", 1)
    student2 = Student("Meikä", "Mandoliini", 2)
    student3 = Student("Johny", "Depp", 3)
    student4 = Student("Bruce", "Springsteen", 4)
    student5 = Student("Johnny", "Cash", 5)
    student6 = Student("Barack", "Obama", 6)
    
    
    my_mammal = Mammal(1, "Fish", "John" ,"massive", "2kg", "40cm", "30cm")
    my2_mammal = Mammal(2, "Squirel", "Jyrsis", "small", "400g", "20cm", "10cm")
    my3_mammal = Mammal(3, "Cat", "Sack", "big", "5kg", "60cm", "30cm")
    my4_mammal = Mammal(4, "Hamster", "Pasi", "small", "40g", "10cm", "5cm")
    my5_mammal = Mammal(5, "Rabbit", "Tero", "Mid-size", "0.5kg", "30cm", "20cm")
    my6_mammal = Mammal(6, "Elephant", "Dumbo", "Very big", "7500kg", "3m", "3m")
    
    database = {student1.__str__(): my_mammal,
                student2.__str__(): my2_mammal, 
                student3.__str__(): my3_mammal,
                student4.__str__(): my4_mammal,
                student5.__str__(): my5_mammal,
                student6.__str__(): my6_mammal
        }
    
    for key, value in database.items():    
        print("\n\nOwner: ", key, "\n\nHis/Her pet: ", value)
    
    
main()
    
    
    
    
    
    
            
                                                                   