from datetime import date
import calendar 

#Opens 2 files so I can add data to them

f1 = open("Lower.txt", "a")
f2 = open("Upper.txt", "a")


today = date.today()
#dd/mm/YY
d1 = today.strftime("%d/%m/%Y")


c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2021, 3)
print(str)

Lower = []
Upper = []

userinput = input("What did your train today? ")

if userinput == "Lower":
    Lower.append(d1 + ", " +  input("How did your training go?: "))
    
if userinput == "Upper":
    Upper.append(d1 + ", " +  input("How did your training go?: "))
    
#print(Legs)
#print(Upper)

str1 = ''.join(Lower)
f1.write(str1)

str2 = ''.join(Upper)
f2.write(str2)

f1.close()
f2.close()