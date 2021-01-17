nlist = []
i = 1
while i <= 10:
    number = input("Enter a number ")
    nlist.append(number)
    i = i+1
print(nlist)

#string list 

alist = []
i = 1 
while i <= 10: 
    string = input("Enter a word ")
    alist.append(string)
    i = i+1
print(alist)

#rlist 

import random 
rlist = []
i = 1 
while i <= 10: 
    rlist.append(random.randint(0,100))
    i =i+1
print (rlist)

#testi

nlist.sort(key=int)

print(nlist)

alist.sort()

print(alist)
