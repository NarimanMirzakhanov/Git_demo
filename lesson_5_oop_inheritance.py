class Dog:
    biology_class = 'Animal'

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color


    def run(self):
        return 'I can run'


    def get_name(self):
        return f"Hello! My name is {self.name}"


dog1 = Dog('Bobik', 3, 'brown')
print(dog1.name)
print(dog1.get_name())
print(dog1.color)
print(dog1.biology_class)

dog2 = Dog('Rex', 7, 'black')
print(dog2.biology_class)
print(dog2.get_name())


# Inheritance (наследование)
class Pitbull(Dog):
    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    def give_a_paw(self):
        return "I can give a paw!"


dog3 = Pitbull('Lassie', 8, 'black', 'type1 ')
print(dog3.get_name())
print(dog3.biology_class)
print(dog3.give_a_paw())
print(dog3.passport)

