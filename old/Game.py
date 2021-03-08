import random
hads = random.randint(1,99)
print('the number is :' ,hads)
javab = input ("b or k or d : ")
x=0
y=0
c=0

while javab!='d':
    c+=1
    if javab=='k':
        x=hads  
        if c==1:
            y=99 
            
    elif javab=='b':
        y=hads
    hads = random.randint(x,y)
    print('the number is :' ,hads)
    javab = input ("b or k or d : ")   
        

print('you did it !')

