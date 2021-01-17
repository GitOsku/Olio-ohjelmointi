class Virhe(Error):
    print("Kivi, Paperi tai Sakset kiitos :)")
    pass

peluripisteet = 0


def laskuri1(f):
    while (peluripisteet < 3): 
        if f > 0:
            peluripisteet += 1
    print("Geimeri voitti")


pclista = 0             
                    
            
def pclaskuri(i): 
    while (pclista < 3):
        if i > 0:
            pclista += 1
    print("Tietskari voitti")
    
            
from random import randint 

l = ["Kivi", "Paperi", "Sakset"]

#main funktion täs alla
def rps(tietskari): 
    
    h = "Hävisit tämän erän!"
    v = "Voitit tämän erän!"
    
    
    geimeri = False 
    
    while geimeri == False:
        try:
            geimeri = input('"Kivi", "Paperi", "Sakset? "') 
            if geimeri != ("Kivi" or "Paperi" or "Sakset"):
                raise Virhe
            if geimeri == tietskari:
                print ("Tasuri!")
            elif geimeri == "Kivi":
                if tietskari == "Paperi": 
                    print(h)
                    pclaskuri(1)
                else:
                    print(v)
                    laskuri1(1)
            elif geimeri == "Paperi":
                if tietskari == "Sakset":
                    print(h)
                    pclaskuri(1)
                else:
                    print(v)
                    laskuri1(1)
            elif geimeri == "Sakset":
                if tietskari == "Kivi":
                    print (h)
                    pclaskuri(1)
                else: 
                    print(v)
                    laskuri1(1)
                
                geimeri = False
                rps(l[randint(0,2)])
    
rps(l[randint(0,2)])
            
                
            
                
            
            
    
        