peluripisteet = 0
pclista = 0

def laskuri(f):
    global pclista
    global peluripisteet
    if f == 0:
        peluripisteet += 1
    elif f == 1:
        pclista += 1
    elif (peluripisteet == 3): 
        print("Geimeri voitti")
        print("Resetoi peli")
        peluripisteet = 0
        pclista = 0
    elif (pclista == 3): 
        print("Tietskari voitti")
        print("Resetoi peli")
        peluripisteet = 0
        pclista = 0

from random import randint 

l = ["Kivi", "Paperi", "Sakset"]

#main funktion täs alla
def rps(tietskari): 
    
    h = "Hävisit tämän erän!"
    v = "Voitit tämän erän!"
    
    
    geimeri = False 
    
    while geimeri == False:
        
            geimeri = input('"Kivi", "Paperi", "Sakset? "') 
            print(geimeri)
           # if geimeri != "Kivi" or geimeri != "Paperi" or geimeri != "Sakset": 
            if geimeri == tietskari:
                print ("Tasuri!")
            elif geimeri == "Kivi":
                if tietskari == "Paperi": 
                    print(h)
                    laskuri(1)
                else:
                    print(v)
                    laskuri(0)
            elif geimeri == "Paperi":
                if tietskari == "Sakset":
                    print(h)
                    laskuri(1)
                else:
                    print(v)
                    laskuri(0)
            elif geimeri == "Sakset":
                if tietskari == "Kivi":
                    print (h)
                    laskuri(1)
                else: 
                    print(v)
                    laskuri(0)
                
            geimeri = False
            rps(l[randint(0,2)])
    

rps(l[randint(0,2)])