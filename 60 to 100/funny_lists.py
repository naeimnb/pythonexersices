funnies = ['fun1', 'fun2', 'fun3', 'fun4']

for fun in funnies:
    message = f"this kind of {fun} is so funny hahahaha"
    print(message)


numbers = list(range(1,11))
print(numbers)

even_nambers = list(range(2,11,2))
print(even_nambers)

odd_numbers = list(range(1,10,2))
print(odd_numbers)

sq_number =list()
for i in range(1,10):
    sq = i ** 2
    sq_number.append(sq)
print(sq_number)

my_list = [i**2 for i in range (1,11)]
print(my_list)
my_sliced_list = my_list[1:8:2]
print(my_sliced_list)


my_tuple = (5,10)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])
for item in my_tuple:
    print(item)
my_tuple = (15,20)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])
for item in my_tuple:
    print(item)
