from Participantfilu import Participant

#from Exercise6p5 import Wolf

#from Exercise6p5 import Bear


class Student(Participant):
    
    def __init__(self, iq, haircolor, OS, moneysupport, rent):
        super().__init__(iq, haircolor, OS)
        self.moneysupport = moneysupport
        self.rent = rent
        
    def __str__(self):
        return "iq: " + format(self.iq)\
            + "\nHaircolor: " + format(self.haircolor)\
            + "\nOS: " + format(self.OS)\
            + "\nMoneysupport: " + format(self.moneysupport)\
            + "\nRent: " + format(self.rent)\
                
class Teacher(Participant):
    
    def __init__(self, iq, haircolor, OS, job, salary):
        super().__init__(iq, haircolor, OS)
        self.job = job
        self.salary = salary
        
    def __str__(self):
        return "iq: " + format(self.iq)\
            + "\nHaircolor: " + format(self.haircolor)\
            + "\nOS: " + format(self.OS)\
            + "\nMoneysupport: " + format(self.job)\
            + "\nRent: " + format(self.salary)\

student = Student("50iq", "blond", "Windows", "Kela", "400€")

teacher = Teacher("200iq", "blond", "Windows", "Teaching", "3000€")

#wolf = Wolf("5", "catanimal", "Silverarrow", "60kg", "notlong", "1.5m", "50cm", "lapland", "day", "other animals", "growls the moon")

#bear = Bear("4", "Körmy", "Nallepuh", "250kg", "Mediumlong", "2.5m", "1.5m", "forest", "wholewinter", "honey", "Muurrrr")

print(student)
print("")
#print("Students animal: ", wolf, "\n\nand", bear)
print("")
print(teacher)  
print("")
#print("Teachers animal: ", wolf, "\n\nand", bear)              