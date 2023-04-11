# Получить список (list) целых чисел
a = '1 2 3 4 5'
b = list(map(int, a.split()))
print(b)
# [1, 2, 3, 4, 5]


# Получить список (list) со строками
a = 'Hello aa 2 3 4 5'
b = list(map(str, a.split()))
print(b)
# ['Hello', 'aa', '2', '3', '4', '5']


def fun(x):
    return x**2


def fun_n(x):
    return x**3


a = [1, 3, 5, 7, -67, -3]
a1 = list(map(str, a)) # Конвертировать целые числа в строки
print(a1)
a2 = list(map(abs, a)) # Вернуть модуль всех элементов
print(a2)
a3 = list(map(fun, a)) # Возведение в квадрат с помощью функции fun()
print(a3)
a4 = list(map(fun_n, a)) # Возведение в куб с помощью функции fun_n()
print(a4)


# Вернуть с помощью функции filter значения больше 5 (a1 - числа, a2 - list, a3 - tuple)
def fun_2(x):
    return x > 5


a = [32, 1, 4, 73, 4, 6]
a1 = filter(fun_2, a)
print(*a1)

a2 = list(filter(fun_2, a))
print(a2)

a3 = tuple(filter(fun_2, a))
print(a3)

