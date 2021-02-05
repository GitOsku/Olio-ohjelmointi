class Car: 


    def __init__(self):
        self.__make = "Toyota"
        self.__model = "Supra"
        self.__mileage = "150000Km"
        self.__price = "30000$"
        self.__color = "Matblack"
        self.__maximum = "200kg"
        self.__trunk = "50l"
        
        #mutators
        
    def set_make(self):
        set_make = input("What manufacturer you want your car to be? ")
        self.__make = set_make
    
    def set_model(self):
        set_model = input("What model do you want? ")
        self.__model = set_model
        
    def set_mileage(self):
        set_mileage = input("How many kilometers does it have? ")
        self.__mileage = set_mileage
        
    
    def set_price(self):
        set_price = input("How much you gonna offer for this? ")
        self.__price = set_price
        
    def set_color(self):
        set_color = input("What calor you want your car to be? ")
        self.__color = set_color
        
    def set_maximum(self):
        set_maximum = input ("How much weight can this handle? ")
        self.__maximum = set_maximum
        
    def set_trunk(self):
        set_trunk = input("How big is the trunk? ")
        self.__trunk = set_trunk
        
    #getters
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price
    
    def get_maximum(self):
        return self.__maximum
    
    def get_trunk(self):
        return self.__trunk
    
    
    def __str__(self):
        return "Maker: " + format(self.__make)\
                + "\nModel: " + format(self.__model)\
                + "\nMileage: " + format(self.__mileage)\
                + "\nPrice: " + format(self.__price)\
                + "\nColor: " + format(self.__color)\
                + "\nMaximum: " + format(self.__maximum)\
                + "\nTrunk: " + format(self.__trunk)\

                    
def main():
    
    my_car = Car()

    my_car.set_make()
    my_car.set_model()
    my_car.set_mileage()
    my_car.set_price()
    my_car.set_color()
    my_car.set_maximum()
    my_car.set_trunk()
    
    
    print(my_car.__str__())


main()
    
    
    
    
    
    
    
