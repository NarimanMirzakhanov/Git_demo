# Create a list

sentence = "Python is awesome"
print(sentence.split(' ', maxsplit=1))
# ['Python', 'is awesome']

my_list = [1, 'hello', 2.0, True, None]
# my_list.append(sentence)
my_list.insert(0, sentence)
print(my_list)
# ['Python is awesome', 1, 'hello', 2.0, True, None]

print(my_list.count(1))  # 2
print(my_list.index(1, 2))  # 4

my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
print(my_list1[-1][-1])  # 5
my_list1.reverse()
print(my_list1)
# [[1, 2, 3, 4, 5], 5, 4, 3, 2, 1]

numbers = [1, 2, 3, 4, 5]
new_list = [i ** 2 for i in numbers if i % 2]
print(new_list)
# [1, 9, 25]
print(*numbers)  # вместо цикла for
# 1 2 3 4 5

number = [i for i in range(10) if i % 2 != 0]
print(number)
# [1, 3, 5, 7, 9]
