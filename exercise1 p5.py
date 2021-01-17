laskin = 0
counter = 0
while True: 
     number = int(input("Enter a number ")) 
     if number > 0 :
         if (number % 2) == 0:
             laskin += 1
     if number < 0 : 
         counter += 1
         if (number % 2) == 0: #tee tälle jotai :D 
             laskin += 1
     if number == 0:
         break
print (counter)
print (laskin)