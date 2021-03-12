def print_double(x):
    print(2 * x)


print_double(3)


def shout(word):
    return word + "!"


speak = shout
output = speak("shout")
print(output)


def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 5
b = 10

print(do_twice(add, a, b))

from math import pi

print(pi)

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break

i = 3
while i >= 0:
    print(i)
    i = i - 1

print("------------------------------------------------")
for i in range(10):
    if not i % 2 == 0:
        print(i + 1)

x = input("number:")
x = int(x)
c = 0
for i in range(1, x):
    if (x % i == 0):
        c += 1
if (c == 1):
    print("okey")

else:
    print("NOT okey")
