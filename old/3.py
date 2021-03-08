maxAge=0
age=0

while (not age<0):
    age=int(input())
    if maxAge<age:
        maxAge=age
print(maxAge)