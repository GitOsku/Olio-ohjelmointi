from Mamelukkikala import Mammal

from Domesticfilu import Domestic

from Domesticfilu import Wild


class Cat(Mammal):


    def __init__(self, id, specie, name, size, weight, height, width, diet, noise):
        super().__init__(id, specie, name, size, weight, height, width)
        self.diet = diet
        self.noise = noise
        
    def __str__(self):
        return "ID: " + format(self.ID)\
            + "\nSpecie: " + format(self.specie)\
            + "\nName: " + format(self.name)\
            + "\nSize: " + format(self.size)\
            + "\nWeight: " + format(self.weight)\
            + "\nHeight: " + format(self.height)\
            + "\nWidth: " + format(self.width)\
            + "\nDiet: " +format(self.diet)\
            + "\nNoise: " + format(self.noise)\
                

class Kangaroo(Mammal):
    
    def __init__(self, id, specie, name, size, weight, height, width, diet, noise):
        super().__init__(id, specie, name, size, weight, height, width)
        self.diet = diet
        self.noise = noise
        
    def __str__(self):
        return "ID: " + format(self.ID)\
            + "\nSpecie: " + format(self.specie)\
            + "\nName: " + format(self.name)\
            + "\nSize: " + format(self.size)\
            + "\nWeight: " + format(self.weight)\
            + "\nHeight: " + format(self.height)\
            + "\nWidth: " + format(self.width)\
            + "\nDiet: " +format(self.diet)\
            + "\nNoise: " + format(self.noise)\
                
        
class Lion(Mammal):
    
    def __init__(self, id, specie, name, size, weight, height, width, diet, noise):
        super().__init__(id, specie, name, size, weight, height, width)
        self.diet = diet
        self.noise = noise
        
    def __str__(self):
        return "ID: " + format(self.ID)\
            + "\nSpecie: " + format(self.specie)\
            + "\nName: " + format(self.name)\
            + "\nSize: " + format(self.size)\
            + "\nWeight: " + format(self.weight)\
            + "\nHeight: " + format(self.height)\
            + "\nWidth: " + format(self.width)\
            + "\nDiet: " +format(self.diet)\
            + "\nNoise: " + format(self.noise)\

class Bear(Domestic):
    
    def __init__(self, id, specie, name, size, weight, height, width, livingarea, sleepingtime, diet, noise):
        super().__init__(id, specie, name, size, weight, height, width, livingarea, sleepingtime)
        self.diet = diet
        self.noise = noise
        
    def __str__(self):
        return "ID: " + format(self.ID)\
            + "\nSpecie: " + format(self.specie)\
            + "\nName: " + format(self.name)\
            + "\nSize: " + format(self.size)\
            + "\nWeight: " + format(self.weight)\
            + "\nHeight: " + format(self.height)\
            + "\nWidth: " + format(self.width)\
            + "\nLivingarea: " +format(self.livingarea)\
            + "\nSleepingtime: " +format(self.sleepingtime)\
            + "\nDiet: " +format(self.diet)\
            + "\nNoise: " + format(self.noise)\
    
class Wolf(Wild):
    
    def __init__(self, id, specie, name, size, weight, height, width, livingarea, sleepingtime, diet, noise):
        super().__init__(id, specie, name, size, weight, height, width, livingarea, sleepingtime)
        self.diet = diet
        self.noise = noise
        
    def __str__(self):
        return "ID: " + format(self.ID)\
            + "\nSpecie: " + format(self.specie)\
            + "\nName: " + format(self.name)\
            + "\nSize: " + format(self.size)\
            + "\nWeight: " + format(self.weight)\
            + "\nHeight: " + format(self.height)\
            + "\nWidth: " + format(self.width)\
            + "\nLivingarea: " +format(self.livingarea)\
            + "\nSleepingtime: " +format(self.sleepingtime)\
            + "\nDiet: " +format(self.diet)\
            + "\nNoise: " + format(self.noise)\
    
def main():

    cat = Cat('1', "Sphynx", "Jätäkki", "long", "3kg", "40cm", "20cm", "catfood", "miau")
    
    kangaroo = Kangaroo("2", "Kangaroo", "Ruu", "Extralong", "150kg", "2m", "1m", "grass", "Punching noises")
    
    lion = Lion("3", "Cat animal", "Mufasa", "Mediumlong", "190kg", "3m", "1m", "Beef", "räyh")
    
    bear = Bear("4", "Körmy", "Nallepuh", "250kg", "Mediumlong", "2.5m", "1.5m", "forest", "wholewinter", "honey", "Muurrrr")
    
    wolf = Wolf("5", "catanimal", "Silverarrow", "60kg", "notlong", "1.5m", "50cm", "lapland", "day", "other animals", "growls the moon")
    
    print(cat)
    print("")
    print(kangaroo)
    print("")
    print(lion)
    print("")
    print(bear)
    print("")
    print(wolf)
    
main()