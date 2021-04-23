class Person:
    def __init__(self, first_name, last_name, age):
        self.name = first_name
        self.family = last_name
        self.age = age

    def say_hello(self):
        print(f"Hello my name is {self.name.title()} and my last name is {self.family.title()}")
        print(f" I am {self.age} years old")

    def __str__(self):
        return (self.family)