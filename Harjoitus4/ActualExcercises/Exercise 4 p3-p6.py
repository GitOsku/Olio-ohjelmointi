from Cellphoneclass import Cellphone

from Dicefilu import Dice


def main():
    
    my_phone = Cellphone(1)
    my2_phone = Cellphone(2)       
    my3_phone = Cellphone(3)   
    my4_phone = Cellphone(4)
    my5_phone = Cellphone(5)
    my6_phone = Cellphone(6) 
    my_dice = Dice()


    #First objects questions

    manufact = input("Whose phone you want: ")
    
    my_phone.setManufact(manufact)
    
    model = input("What model you want: ")
    my_phone.setModel(model)
    
    retailprice = input("How much you wanna pay for that: ")
    my_phone.setRetailprice(retailprice)
    
    
    
    print("")
    #Here is the second object's questions
    
    manufact = input("Whose phone you want: ")
    my2_phone.setManufact(manufact)
    
    
    model = input("What model you want: ")
    my2_phone.setModel(model)
    
    retailprice = input("How much you wanna pay for that: ")
    my2_phone.setRetailprice(retailprice)
    
    
    
    print("")
    #Third's phone questions
    
    manufact = input("Whose phone you want: ")
    my3_phone.setManufact(manufact)
    
    
    model = input("What model you want: ")
    my3_phone.setModel(model)
    
    retailprice = input("How much you wanna pay for that: ")
    my3_phone.setRetailprice(retailprice)
    
    #4th objects questions
    
    manufact = input("Whose phone you want: ")
    my4_phone.setManufact(manufact)
    
    
    model = input("What model you want: ")
    my4_phone.setModel(model)
    
    retailprice = input("How much you wanna pay for that: ")
    my4_phone.setRetailprice(retailprice)
    
    #fifth
    
    manufact = input("Whose phone you want: ")
    my5_phone.setManufact(manufact)
    
    
    model = input("What model you want: ")
    my5_phone.setModel(model)
    
    retailprice = input("How much you wanna pay for that: ")
    my5_phone.setRetailprice(retailprice)
    
    
    #6th
    
    manufact = input("Whose phone you want: ")
    my6_phone.setManufact(manufact)
    
    
    model = input("What model you want: ")
    my6_phone.setModel(model)
    
    retailprice = input("How much you wanna pay for that: ")
    my6_phone.setRetailprice(retailprice)
    
    print(my_dice.toss()) #prove that it works :D
    
    #dice terms
    
    if my_dice.roll == 1:
        print (my_phone)
    
    elif my_dice.roll == 2:
        print (my2_phone)
    
    elif my_dice.roll == 3:
        print(my3_phone)
        
    elif my_dice.roll == 4:
        print(my4_phone)
        
    elif my_dice.roll == 5:
        print (my5_phone)
        
    elif my_dice.roll == 6:
        print(my6_phone)
        
    else: 
        print ("Why dis no work :D")
        


main()