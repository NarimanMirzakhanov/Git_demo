class Family:

    def __init__(self, member, name, age):
        self.member = member
        self.name = name
        self.age = age

    def get_describe(self):
        return f"Hello, my name is {self.name}. I'm {self.member} and I'm {self.age} years old"


father = Family('father', 'Nariman', 40)
print(father.get_describe())
mother = Family('mother', 'Irina', 35)
print(mother.get_describe())
son = Family('son', 'Abdulla', 6)
print(son.get_describe())
daughter = Family('daughter', 'Amelia', 4)
print(daughter.get_describe())


class BigFamily(Family):

    def __init__(self, member, name, age, relation):
        super().__init__(member, name, age)
        self.relation = relation

    def get_describe(self):
        return f"Hello, my name is {self.name}. I'm {self.relation} and I'm {self.age} years old"


brother = BigFamily('father', 'Arsen', 37, 'brother')
print(brother.get_describe())




