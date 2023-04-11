# def fun(x):
#     return x**3
#
#
# print(fun(3))
#
# # можно эту функцию написать с помощью лямбда функции
# a = lambda x: x** 3
# print(a(3))

s = lambda x: x * x
print(s(4))

a = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(a(5))

# Сортировка сначала по четным числам
a = [43, 54, 75, 53, 100]
print(sorted(a, key=lambda x: x % 2))
# [54, 100, 43, 75, 53]

# Сортировка по алфавиту
a = ['hello', 'aaa', 'bbb', 'xxx', 'nnn']
print(sorted(a, key=lambda x: x))
# ['aaa', 'bbb', 'hello', 'nnn', 'xxx']


# Сортировка по второму значению
a = [(1, 2), (2, 1), (3, 3)]
print(sorted(a, key=lambda x: x[1]))
# [(2, 1), (1, 2), (3, 3)]

a = [(1, 'ff'), (2, 'cc'), (3, 'aa')]
print(sorted(a, key=lambda x: x[1]))
# [(3, 'aa'), (2, 'cc'), (1, 'ff')]

# Сортировка сначала по первому, а потом по второму значению
a = [(1, 'ff'), (2, 'cc'), (1, 'aa')]
print(sorted(a, key=lambda x: (x, x[1])))
# [(1, 'aa'), (1, 'ff'), (2, 'cc')]


# Использование key без lambda
def fun(num):
    return num % 10


a = [4, 10, 43, 90, 34, 8]
print(sorted(a, key=fun))

a = [40, 34, 64, 12, 70, 45]
print(sorted(a, key=lambda x: x % 10))

# Сортировка по цифрам (второй элемент каждого элемента)
a = ['qqq 23', 'aaa 12', 'rrr 8']
print(sorted(a, key=lambda x: int(x.split()[1])))

# Сортировка по буквам (первый элемент каждого элемента)
a = ['qqq 23', 'aaa 12', 'rrr 8']
print(sorted(a, key=lambda x: x.split()[0]))


# Сортировка по первым значениям потом по вторым (по возрастанию)
a = ['qqq 23', 'qqq 12', 'rrr 8']
print(sorted(a, key=lambda x: (x.split()[0], int(x.split()[1]))))


# Сортировка по первым значениям потом по вторым (по убыванию)
a = ['qqq 23', 'qqq 12', 'rrr 8']
print(sorted(a, key=lambda x: (x.split()[0], -int(x.split()[1]))))
