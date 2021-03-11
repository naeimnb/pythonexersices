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



tedade_student=int(input(''))

amare_sen=input('').split()
if len(amare_sen)!=tedade_student:
    amare_sen=amare_sen[:-1]

amare_ghad=input('').split()
if len(amare_ghad)!=tedade_student:
    amare_ghad=amare_ghad[:-1]

amare_vazn=input('').split()
if len(amare_vazn)!=tedade_student:
    amare_vazn=amare_vazn[:-1]


#for sen_stu in amare_sen:
#    for ghad_stu in amare_ghad:
#        for vazn_stu in amare_vazn:
#            Student(sen_stu,ghad_stu,vazn_stu)
#print(Student.average_sen())