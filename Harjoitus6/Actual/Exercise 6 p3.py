from Mamelukkikala import Mammal


class Cat(Mammal): #inherits mammal

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
                

class Kangaroo(Mammal): #inherits mammal
    
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
                
        
class Lion(Mammal): #inherits mammal
    
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


cat = Cat('1', "Sphynx", "Jätäkki", "long", "3kg", "40cm", "20cm", "catfood", "miau")

kangaroo = Kangaroo("2", "Kangaroo", "Ruu", "Extralong", "150kg", "2m", "1m", "grass", "Punching noises")

lion = Lion("3", "Cat animal", "Mufasa", "Mediumlong", "190kg", "3m", "1m", "Beef", "räyh")

print(cat)
print("")
print(kangaroo)
print("")
print(lion)
