class Student:
    count=0
    sum_sen=0
    sum_ghad=0
    sum_vazn=0
    ave_sen=0
    ave_ghad=0
    ave_vazn=0
    def __init__(self,sen,ghad,vazn):
        self.sen=float(sen)
        self.ghad=float(ghad)
        self.vazn=float(vazn)
        Student.count+=1
        Student.sum_sen+=self.sen
        Student.sum_ghad+=self.ghad
        Student.sum_vazn+=self.vazn
        Student.ave_sen=Student.sum_sen/Student.count
        Student.ave_ghad=Student.sum_ghad/Student.count
        Student.ave_vazn=Student.sum_vazn/Student.count
    def average_sen(self):
        return(Student.ave_sen)
    def average_ghad(self):
        return(Student.ave_ghad)
    def average_vazn(self):
        return(Student.ave_vazn)

naeim=Student(33,180,100)
ali=Student(34,180,70)

print(ali.average_vazn())