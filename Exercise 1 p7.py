

def ap_func(): 

    summa = 0
    sumu = 0
    the_squared_sum = 0
    a = int(input("Anna ensimmäinen luku "))
    d = int(input("Anna valinumero kiitos "))
    n = int(input("Kuinka monta numeroa saisi olla "))
    print("Tässä olisi aritmeettiset perkeleet ")
    
    m = 1
    while (m <= n):
        
        tm = a +(m - 1) * d
       
        print (tm)
       
        m = m + 1
       
        if (tm % 2) == 0:
            sumu += 1
        
        if (tm % 2) == 0:
            the_squared_sum += tm ** 2
            
        if (tm % 2) == 0:
            summa += tm 
    
    print (sumu) #aritmeettisten numerojen määrä
    print (the_squared_sum) # 
    print (summa) 
    

ap_func()