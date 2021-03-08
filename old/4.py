max=0
max2=0

num=int(input(''))
while num>0:
    if max>num:
        if max2<num:
            max2=num
    else:
        max2=max
        max=num
    num=int(input(''))
print(max, max2)