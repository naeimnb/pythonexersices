def standardName (name):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    name=name.lower()
    for alpha in alphabet:
        startw=name.startswith(alpha)
        if startw==True:
            name = name[1:]
            name= alpha.upper()+name
            return name

name1= input('')
name2= input('')
name3= input('')
name4= input('')
name5= input('')
name6= input('')
name7= input('')
name8= input('')
name9= input('')
name10= input('')

print(standardName(name1))
print(standardName(name2))
print(standardName(name3))
print(standardName(name4))
print(standardName(name5))
print(standardName(name6))
print(standardName(name7))
print(standardName(name8))
print(standardName(name9))
print(standardName(name10))