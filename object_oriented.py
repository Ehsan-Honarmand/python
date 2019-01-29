# object oriented programming ---> shey garaiee : OOP 
# <class '__main__.person'> 
# method ehsan.
# count ---> class variable
# name , age ---> object variable
class person:
    count = 0
    def __init__(self , name , age):
        self.name = name 
        self.age = age
        person.count = person.count + 1
    def get_name(self):
        print('name is %s' % self.name)
    def get_age(self):
        print('age is %i' % self.age)
    def get_info(self):
        print('name is %s and age is %i ' %(self.name , self.age))
    def birthday(self):
        self.age = self.age + 1
        print('happy birthdat %s' %self.name)
    def return_count(self):
        return person.count

ehsan = person('ehsan',27)
ehsan.get_name()

ehsan.get_info()
ehsan.birthday()
ehsan.get_age()

print(type(ehsan))

manooch = person('manoochehr',18)
manooch.get_info()

print('at the moment I have %i persons' %ehsan.return_count())
