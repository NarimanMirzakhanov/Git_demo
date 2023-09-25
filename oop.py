class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age


    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'


    def walk(self):
        return 'I can walk!'


    def set_name(self, new_name):
        self.name = new_name



person_1 = Person('Nariman', 'Mirzakhanov', 40)
print(person_1.name)
print(person_1.surname)
print(person_1.hello())
print(person_1.walk())
person_1.name = 'Abdulla'
print(f'New name is {person_1.name}')
# print(person_1.age)
print(Person.__dict__)
print(f'Attributes: {person_1.__dict__}')
print(person_1._Person__age)
person_1.set_name('Amelia')
print(person_1.hello())
print()
person_2 = Person('Irina', 'Omarieva', 35)
print(person_2.name)
print(person_2.surname)
print(person_2.hello())
print(person_2.walk())
print()


class Tester(Person):

    def __init__(self, name, surname, framework, age):
        super().__init__(name, surname, age)
        self.framework = framework

    def test(self):
        return 'I love testing'


tester_1 = Tester('Max', 'Popov', 'pytest', 55)
print(tester_1.name)
print(tester_1.framework)
print(tester_1.hello())
print(f'Tester: {tester_1.__dict__}')
