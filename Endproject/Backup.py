from datetime import date
import calendar 

class Stash:

    def __init__(self, f1, f2, f3):
        self.f1 = open("Squat.txt", "a")
        self.f2 = open("Bench.txt", "a")
        self.f3 = open("Deadl.txt", "a")
        
        self.f1 = f1 
        self.f2 = f2
        self.f3 = f3
        
        
#Opens 2 files so I can add data to them

    
    today = date.today()
    #dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    
    
    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(2021, 4)
    print(str)
    
    Squat = []
    Bench = []
    Deadl = []
    
    userinput = input("What did your train today? ")
    
    #when inputting amount of sets use "*" ty
    
    if userinput == "Squat":
        Squat.append(d1 + ", " +  input("How many sets did you do?: "))
        Squat.append(", " + input("How much weight did you use?: "))
        
    if userinput == "Bench":
        Bench.append(d1 + ", " +  input("How many sets did you do?: "))
        Bench.append(", " + input("How much weight did you use?: "))
        
    if userinput == "Deadl":
        Deadl.append(d1 + ", " +  input("How many sets did you do? : "))
        Deadl.append(", " + input("How much weight did you use?: "))
        
        
    #print(Legs)
    #print(Upper)
    
    str1 = ''.join(Squat) + "\n"
    f1.write(str1)
    
    str2 = ''.join(Bench) + "\n"
    f2.write(str2)
    
    str3 = ''.join(Deadl) + "\n"
    f3.write(str3)
    
    
    f1.close()
    f2.close()
    f3.close()