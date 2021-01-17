vihko = 0
laskin = 0
counter = 0

while True: 
     number = int(input("Enter a number ")) 
     if number > 0 :
         if (number % 2) == 0:
             laskin += 1 #exercise 4 
     if number < 0 : 
         counter += 1
         if (number % 2) == 0: 
             laskin += 1 #exercise 5 
     if number > 0 : 
         if (number % 3) == 0:
             vihko += 1 #exercise 6 
     if number == 0: #tää on kill switch 
         break

print (counter) # negatiiviset
print (laskin) #even steven 
print (vihko) # kolmella jaolliset