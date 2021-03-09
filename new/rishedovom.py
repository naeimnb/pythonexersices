import math

tedad = int(input(''))
lst_adade_varede=list()
adad=0
for i in range(0,tedad):
    adad=int(input(''))
    lst_adade_varede.append(adad)

for num in lst_adade_varede:
    res_adad=math.sqrt(num)
    res_adad=f'{res_adad:.5f}'[:-1]
    print(res_adad)