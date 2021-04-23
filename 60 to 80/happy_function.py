def say_hi(name):
    return (f"Hello {name.title()}")


def say_hi_again(naei, age=20):
    return (f"hello {naei.title()} you are {age} jare alt")


def person_again(first_name, last_name):
    person = f"{first_name.title()} {last_name.title()}"
    return person


def person (first_name, last_name):
    person_dictionary = {
        'First_Name' : first_name.title(),
        'Last_Name' : last_name.title()
    }
    return person_dictionary

def my_item (*item):
    return (item)

greeting = say_hi('ali')
print(greeting)
say_hi('naeim')

again_greeting = say_hi_again('milad')
print(again_greeting)
say_hi_again('rasol', 30)
say_hi_again(age=30, naei='keyvan')

new_person = person_again('naeim', 'nobahari')
print(new_person)

dic_person = person('Rasol', 'rasolian')
print(dic_person)
for item in dic_person.values():
    print(item)

my_item('item1','item2', 33)
print(type(my_item(1,2,3)))