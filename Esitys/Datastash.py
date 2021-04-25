from datetime import date
import calendar 


#asks the inputs from user, and adds the data to corrrect files.


class Stash:

    def Adder(username):
#Opens 2 files so I can add data to them

        f1 = open(username + "/Squat.txt", "a")
        f2 = open(username + "/Bench.txt", "a")
        f3 = open(username + "/Deadl.txt", "a")
        
        
        today = date.today()
        #dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        
        #this was kinda useless and didn't know what to do with it.
        
        c = calendar.TextCalendar(calendar.MONDAY)
        str = c.formatmonth(2021, 3)
        print(str)
        
        Squat = []
        Bench = []
        Deadl = []
        
        userinput = input("What did your train today? ")
        
        #user input gets saved into strings.
        
        #when inputting amount of sets use "*" thank you
        
        if userinput == "Squat":
            Squat.append(d1 + ", " +  input("How many sets did you do?: "))
            Squat.append(", " + input("How much weight did you use?: "))
            
        if userinput == "Bench":
            Bench.append(d1 + ", " +  input("How many sets did you do?: "))
            Bench.append(", " + input("How much weight did you use?: "))
            
        if userinput == "Deadl":
            Deadl.append(d1 + ", " +  input("How many sets did you do? : "))
            Deadl.append(", " + input("How much weight did you use?: "))
                        
        #writes into files 

        str1 = "\n" + ''.join(Squat)
        f1.write(str1)
        
        str2 = "\n" + ''.join(Bench)
        f2.write(str2)
        
        str3 = "\n" + ''.join(Deadl)
        f3.write(str3)
        
        
        f1.close()
        f2.close()
        f3.close()