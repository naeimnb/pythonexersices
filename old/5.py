def maghsom(num):
    maghsom=0
    c=1
    for i in range (1,num):
        maghsom=num%i
        if maghsom==0:
            c+=1
    return c

adad=0
tmax=0
for i in range(1,20):
    numi = int(input(''))
    tmaghsom = maghsom(numi)
    if tmax<tmaghsom:
        tmax=tmaghsom
        adad=numi

print(adad, tmax)