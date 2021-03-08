emtiaz=0
majmoEmtiaz=0
bord=0

for i in range(1,31):
    emtiaz = int(input())
    majmoEmtiaz += emtiaz
    if emtiaz ==3:
        bord +=1
print(majmoEmtiaz,bord)