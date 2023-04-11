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
dog2 = Dog('Rex', 7, 'black')


# Inheritance (наследование)
class Pitbull(Dog):
    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    def give_a_paw(self):
        return "I can give a paw!"

    def run(self):
        return 'I can run fast!'


dog3 = Pitbull('Lassie', 8, 'black', 'type1 ')
print(dog2.run())
print(dog3.run())
