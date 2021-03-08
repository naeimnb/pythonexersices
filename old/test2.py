myString=input('')
c1=0
c2=0
c3=0
newString=''

for element in myString:
    if element == '1':
        c1 +=1
    elif element == '2':
        c2 +=1
    elif element == '3':
        c3 +=1

for i in range (0,c1):
    newString = newString+'1'
    if c3==0:
        if c2==0:
            if i<(c1-1):
                newString = newString+'+'
    else:
        newString = newString+'+'

for i in range (0,c2):
    newString = newString+'2'
    if c3==0:
        if i<(c2-1):
            newString = newString+'+'
    else:
        newString = newString+'+'

for i in range (0,c3):
    newString = newString+'3'
    if i < (c3-1):
        newString = newString+'+'

print(newString)