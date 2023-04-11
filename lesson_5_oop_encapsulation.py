class Dog:
    biology_class = 'Animal'

    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color

    def run(self):
        return 'I can run'

    def get_name(self):
        return f"Hello! My name is {self.__name}"

    def __set_name__(self, new_name):
        self.__name = new_name


dog1 = Dog('Bobik', 3, 'brown')
dog2 = Dog('Rex', 7, 'black')
print(dog2.get_name())
print(dog2.__dict__)
dog2.__set_name__('Snoopy')
print(dog2.get_name())
print(dog2.__dict__)
print(dog2._Dog__name)


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
