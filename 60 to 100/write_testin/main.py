from full_name import full_name

name = full_name('naeim', 'nobahari')
print(name)

print('type q any time you want to exite the loop')
while True:
    name = input('your first name is : ')
    family = input('your last name is : ')
    if name == 'q' or family == 'q':
        break
    else:
        name = full_name(name, family)
        print(name)