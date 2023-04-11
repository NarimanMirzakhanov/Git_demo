# def calc(a, b=4):
#     return a * b
#
#
# print(calc(b=5, a=10))


# def person(age, first_name, last_name):
#     return f"Hello, my name is {first_name} {last_name}, I'm {age} years old"


# print(person(25, 'Anna', 'Smith'))
# print(person(first_name='Anna', last_name='Smith', age=25))


# def person(first_name, last_name, age=20):
#     return f"Hello, my name is {first_name} {last_name}, I'm {age} years old"
#
#
# print(person('Anna', 'Smith'))


# Встроенные функции
print(sum([2, 3, 5, 1, 7]))
print(min(5, 3, 1, 8, -1))


def pattern(length, char2, char1='*'):
    return (char1 + char2) * length + char1


print(pattern(char2='/', length=8))