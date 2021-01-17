counter = 0
while True: 
     number = int(input("Enter a number ")) 
     if number > 0 :
         continue 
     if number < 0 : 
         counter += 1 
     else:
         break
print (counter)