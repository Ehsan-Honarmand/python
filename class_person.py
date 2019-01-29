
class person:
    count = 0
    def __init__(self , name , age):
        self.name = name
        self.age = age
        person.count += 1
    def get_name(self):
        print('name is %s' %self.name)
    def get_age(self):
        print('age is %i'%self.age)
    def get_info(self):
        print('name is %s and age is %i' %(self.name,self.age))
    def birthday(self):
        print('Happy Birthday !!! %s' %self.name)
        self.age += 1
        print('age is %i' % self.age)
    def counter(self):
        return person.count

esi = person('ehsan',27)
print(esi)

esi.get_name()
esi.get_age()
print('I have %i person' %esi.counter() )

esi.birthday()

sami = person('samira',25)
sami.get_info()

print('I have %i person' % sami.counter() )