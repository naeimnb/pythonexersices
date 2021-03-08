lst_loght=list()
num_loghat=int(input(''))
en2fa=dict()
newjomle=''
for i in range(0,num_loghat):
    str_loghat=input('')
    lst_loght=str_loghat.split()
    en2fa[lst_loght[0]] = lst_loght[1]

jomle=input('')
lst_kalamat=jomle.split()
lst_values=en2fa.keys()
for kalame in lst_kalamat:
    if kalame in lst_values:
        tarjome=en2fa[kalame]
        newjomle = newjomle + tarjome + ' '
    else:
        newjomle = newjomle + kalame + ' '

print(newjomle)