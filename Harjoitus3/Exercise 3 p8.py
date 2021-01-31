class Cellphone: 
    
    def __init__(self):
        self.manufact = "Apple"
        self.model = "Iphone 7"
        self.retailprice = "500$"
        
    def setManufact(self, manufact):
        self.manufact = manufact
        
    def getManufact(self):
        return self.manufact
    
    def setModel(self, model):
        self.model = model
        
    def getModel(self):
        return self.model
    
    def setRetailprice(self, retailprice):
        self.retailprice = retailprice
        
    def getRetailprice(self):
        return self.retailprice
        
        
def main():
    
    
    my_phone = Cellphone()
    
    manufact = input("Whose phone you want: ")
    my_phone.setManufact(manufact)
    
    
    model = input("What model you want: ")
    my_phone.setModel(model)
    
    retailprice = input("How much you wanna pay for that: ")
    my_phone.setRetailprice(retailprice)
    
    
    print("Here is the data you provided: " )
    print("Manufact: ", my_phone.getManufact())
    print("Model: ", my_phone.getModel())
    print("Retailprice", my_phone.getRetailprice())
    
    
    
main()