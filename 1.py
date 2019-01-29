# class ---> Computer
# class ---> laptop  
# Computer <----inherit----> laptop (b ers bordan)

class Computer:
    def __init__(self , ram , hard , cpu):
        self.ram = ram 
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram+ self.hard +self.cpu

class laptop(Computer):
    pass

class rasperypie(Computer):
    def value(self):
        return self.ram+ self.hard + self.cpu + self.size


pc1 = Computer(4,8,6)
pc2 = Computer(8,6,4)
print(pc1.value())
print(pc2.value())

laptop1 = laptop(4,8,9)
print(laptop1.value())

rasperypie1 = rasperypie(8,4,6)
rasperypie.size = 13
print(rasperypie1.value())