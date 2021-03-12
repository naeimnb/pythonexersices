class StudentA:
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
        StudentA.count+=1
        StudentA.sum_sen+=self.sen
        StudentA.sum_ghad+=self.ghad
        StudentA.sum_vazn+=self.vazn
        StudentA.ave_sen=StudentA.sum_sen/StudentA.count
        StudentA.ave_ghad=StudentA.sum_ghad/StudentA.count
        StudentA.ave_vazn=StudentA.sum_vazn/StudentA.count
    def average_sen(self):
        return(StudentA.ave_sen)
    def average_ghad(self):
        return(StudentA.ave_ghad)
    def average_vazn(self):
        return(StudentA.ave_vazn)


class StudentB:
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
        StudentB.count+=1
        StudentB.sum_sen+=self.sen
        StudentB.sum_ghad+=self.ghad
        StudentB.sum_vazn+=self.vazn
        StudentB.ave_sen=StudentB.sum_sen/StudentB.count
        StudentB.ave_ghad=StudentB.sum_ghad/StudentB.count
        StudentB.ave_vazn=StudentB.sum_vazn/StudentB.count
    def average_sen(self):
        return(StudentB.ave_sen)
    def average_ghad(self):
        return(StudentB.ave_ghad)
    def average_vazn(self):
        return(StudentB.ave_vazn)
   
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
    
for i in range(0, tedade_student):
    #print(amare_sen[i],amare_ghad[i],amare_vazn[i])
    A=StudentA(amare_sen[i],amare_ghad[i],amare_vazn[i])



 

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
    
for i in range(0, tedade_student):
    #print(amare_sen[i],amare_ghad[i],amare_vazn[i])
    B=StudentB(amare_sen[i],amare_ghad[i],amare_vazn[i])
    

print(A.average_sen())
print(A.average_ghad())
print(A.average_vazn())

print(B.average_sen())
print(B.average_ghad())
print(B.average_vazn())