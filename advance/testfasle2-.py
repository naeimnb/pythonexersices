class Computer:
    count=0
    def __init__(self, ram, hard, cpu):
        self.ram=ram
        self.hard=hard
        self.cpu=cpu
    def valu(self):
        return(self.ram+self.hard+self.cpu)

class Laptop(Computer):
    def __init__(self, )


pc1=Computer(12, 2, 4)
pc2=Computer(12,1,6)
print(pc1.valu())
print(pc2.valu())


