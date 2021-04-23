my_dictionary = {'name': 'naeim', 'age': 33}
print(my_dictionary['name'])
print(my_dictionary['age'])
print(type(my_dictionary))
print(my_dictionary)
my_dictionary['family'] = 'nobahari'
print(my_dictionary)
for item in my_dictionary:
    print(f"your  {item}  is  {my_dictionary[item]}")
del my_dictionary['family']
print(my_dictionary)
for item in my_dictionary:
    print(f"your  {item}  is  {my_dictionary[item]}")

my_final_dictionary = {
    'age' : 33,
    'name' : 'his name',
    'family name' : 'his family name'
}
print(my_final_dictionary)
for item in my_final_dictionary:
    print(f"your  {item}  is  {my_final_dictionary[item]}")

my_funny_resault = my_dictionary.get('age', 'no age')
print(my_funny_resault)
my_funny_resault = my_final_dictionary.get('sex', 'not set')
print(my_funny_resault)

print(my_dictionary.items())
for  i, j in my_dictionary.items():
    print(f"i is {i} an j is {j}")


new_dictionary = {
    'abc' : '123',
    'def' : '456',
    'ghi' : '789',
}

print('-------------------------------------------')
for key in new_dictionary:
    print(key)
print('-------------------------------------------')
for key in new_dictionary.keys():
    print(key)
print('-------------------------------------------')
for value in new_dictionary.values():
    print(value)
print('-------------------------------------------')
for key,value in new_dictionary.items():
    print(f"{value} = {key}")

print('-------------------------------------------')

test_dictionary1 = {
    'abc' : '123',
    'def' : '456',
    'ghi' : '789',
}
test_dictionary2 = {
    'abcd' : '1234',
    'defg' : '4567',
    'ghij' : '7890',
}

test_list = list()
test_list.append(test_dictionary1)
test_list.append(test_dictionary2)
print(test_list)