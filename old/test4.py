chat=input('')
c=0
for char in chat:
    if (c==0) and (char=='h'):
        c +=1
    elif (c==1) and (char=='e'):
        c +=1
    elif (c==2) and (char=='l'):
        c +=1
    elif (c==3) and (char=='l'):
        c +=1
    elif (c==4) and (char=='o'):
        c +=1
    

if c==5:
    print('YES')
else:
    print('NO')