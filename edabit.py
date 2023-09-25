my_tuple = 1, 2, 3
print(type(my_tuple))
my_tuple2 = ('lemon', 'apple', 'cherry', 'mango')
print(type(my_tuple2))
my_tuple3 = ('mango', )
print(type(my_tuple3))


def sum_it(*args):
    return sum(args)


print(sum_it(2, 5, 7, 8, 56, 34))


def mult(x, y):
    return sum_it(5, 2) * sum_it(10, 10)


print(mult(5, 10))


my_dict = {
    'name': 'Nariman',
    'last_name': 'Mirzakhanov',
    'age': 40,
    'department': 'Quality Assurance'
}

my_dict['salary'] = 5000
print(my_dict)
print(my_dict.pop('salary'))
print(my_dict)
print(my_dict.get('salary', 'Not found'))
print()
print(my_dict['name'])
print(my_dict['last_name'])
my_dict['department'] = 'Software Engineering'
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())


def keywords(**kwargs):
    return kwargs


print(keywords(name='Irina', last_name='Omarieva'))


my_set = {1, 3, 5, 8, 6, 5, 3, 1, 0, 9}
print(my_set)

my_list = (1, 3, 5, 8, 6, 5, 3, 1, 0, 9)
print(my_list)
my_set2 = set(my_list)
print(my_set2)


set1 = {1, 2, 3, 'one', 'ten'}
set2 = {1, 2, 3, 'one', 'ten', 100, 525}
set3 = {1, 2, 3}

print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.intersection(set1))
print(set2.difference(set1))
print(set1)
set1.remove(1)
print(set1)
set1.add(8)
print(set1)
fs = frozenset({1, 2, 3})
print(fs)
