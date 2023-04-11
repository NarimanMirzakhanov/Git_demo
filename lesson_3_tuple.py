# my_tuple = 1, 2, 3
# print(my_tuple)
#
# second_tuple = (12, 'name', True, None, 23, 'name')
# print(second_tuple)
# # (12, 'name', True, None, 23, 'name')
# print(second_tuple.index('name'))  # 1
# print(second_tuple.count('name'))  # 2
# for (index, item) in enumerate(second_tuple):
#     print(index, item)
# # 0 12
# # 1 name
# # 2 True
# # 3 None
# # 4 23
# # 5 name
#
# i = 0
# while i < len(second_tuple):
#     print(i, second_tuple[i])
#     i += 1
# # 0 12
# # 1 name
# # 2 True
# # 3 None
# # 4 23
# # 5 name
#
# result = tuple([item for item in second_tuple if isinstance(item, int)])
# print(result)
# # (12, True, 23)
#
# # # Tuple methods
# print(f'Sum is: {sum(result)}')  # Sum is: 36
# print(f'Max is: {max(result)}')  # Max is: 23
# print(f'Min is: {min(result)}')  # Min is: True
# print(f'Length of my tuple is: {len(my_tuple)}')  # Length of my tuple is: 3
# print(f'Length of resuly is: {len(result)}')  # Length of resuly is: 3
#
# third_tuple = 'Mike',
# print(third_tuple)
# # ('Mike',)
# print(type(third_tuple))
# # <class 'tuple'>
#
# other_tuple = ('banana', 'apple', 'cat')
# a, b, c = other_tuple
# print(a, b, c, sep=', ')
# # banana, apple, cat
#
# letters = list(other_tuple)
# letters[0] = 'ananas'
# print(letters)
# # ['ananas', 'apple', 'cat']
#
# # Nested list in tuple
# fruits = ('apple', ['ananas', 'mango'], 'melon')
# fruits[1][0] = 'cherry'
# print(fruits)
# # ('apple', ['cherry', 'mango'], 'melon')
#
# # swaping variables
# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')

def sum_it(*args):
    total = 0
    for num in args:
        total = total + num
    return total


print(sum_it(4, 5, 10, 6, 20))


def func(*args):
    l = []
    print(len(args))
    for item in args:
        l.append(item * item)
    return l


print(func(2, 5, 6, 8, 10))

