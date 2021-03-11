class person:
    count =0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        person.count+=1
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)
    def print_info(self):
        print("Name is %s  and age is %i"  %(self.name , self.age))
    def brithday(self):
        self.age=self.age+1
        print('happy Birthday')
    def recount(self):
        return(person.count)

jadi = person('jadi',31)
jadi.print_name()
jadi.print_age()
jadi.print_info()
manochehr=person('manoch', 40)
manochehr.print_info()
manochehr.brithday()
manochehr.print_info()
print(jadi.recount())
