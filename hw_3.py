# # Task 3.1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])
#
# # Task 3.2
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = 0
# for i in list_1:
#     if type(i) == int:
#         sum += i
# print(sum)
#
# new_list = []
# print([i for i in list_1 if type(i) == str if i.__contains__('a')])
#
# # Task 3.3
# list_pets = ['cat', 'dog', 'horse', 'cow']
# tuple_pets = tuple(list_pets)
# print(tuple_pets)
# print(type(tuple_pets))

# # Task 3.4
family_1 = input("Введите членов семьи №1: ").split(', ')
family_2 = input("Введите членов семьи №2: ").split(', ')
print(family_1)
print(family_2)
if len(family_1) > len(family_2):
    print("family_1 больше")
elif len(family_1) < len(family_2):
    print("family_2 больше")
else:
    print('Equal')

# # Task 3.5
# film = {
#     'title': "Training Day",
#     'director': 'Antoine Fuqua',
#     'year': 2001,
#     'budget': 45_000_000,
#     'main_actor': "Denzel Washington",
#     'slogan': "To Protect The Sheep You Gotta Catch The Wolf, And It Takes A Wolf To Catch A Wolf."
# }
# print(f"The keys are: {film.keys()}")
# print(f"The values are: {film.values()}")
# print(f"The keys and values of film are: {film}")
#
# # Task 3.6
# my_dictionary = {
#     'num1': 375,
#     'num2': 567,
#     'num3': -37,
#     'num4': 21
# }
# print(sum(my_dictionary.values()))
#
# # Task 3.7
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(my_list))
#
# # Task 3.8
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, '1', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print((set1.issubset(set2)))
# print((set2.issubset(set1)))