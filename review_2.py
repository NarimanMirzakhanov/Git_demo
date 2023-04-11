
# s = "Hello world"
# print(s.replace('l', '?', 2))

# print(s.count('o'))

# w = 'Мирзаханов Нариман Джанбулатович'
# print(w.split())
# print(w.split('и'))

# w1 = '1, 2, 3, 4, 5'
# print(w1.split(','))
# print(w1.split(',', maxsplit=2))

# w2 = w1.split(',')
# print(''.join(w1))

# w3 = '    123hello123    '
# print(w3)
# print(w3.strip().strip('123'))

# w4 = 'hello world'
# print(w4.find('e'))
# print(w4.find('o', 2, 5))

# print(w4.index('o', 2, 5))

# w5 = 'My name is Nariman'
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print((w5.swapcase()))

# w6 = 'qwerty'
# w7 = 'Qwerty'
# w8 = '1234'
# print(w6.islower())
# print(w7.isupper())
# print(w7.isalpha())
# print(w8.isdigit())


# a = int(input("Enter a number: "))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f"{a} делится на 2 и на 10")
#     else:
#         print(f"{a} делится на 2, но не делится на 10")
# else:
#     print(f"{a} не делится на 2")


# number = int(input("Enter a number: "))
# if number < 10:
#     print('Однозначное число')
# elif 10 <= number <= 99:
#     print("Двузначное число")
# elif 100 <= number <= 999:
#     print("Трехзначное число")
# else:
#     print("Мы это еще не проходили")


# x, y = 55, 50
# s = x if x > y else y
# print(s)

# value = 6
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print('Такой цифры нет')


# c = 0
# while c < 5:
#     if c % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')
#     c += 1


# text = int(input('Enter a number: '))
# count = 0
# while text != 'stop':
#     num = int(text)
#     count += num
#     text = input('Для продолжения введите число, если не хотите, то введите stop')
# print(f"Сумма чисел равно {count}")


# num = 10
# for i in range(1, num + 1, 2):
#     print(i)


string_1 = 'Hello'
for i in range(len(string_1)):
    if string_1[i].islower():
        print(i, string_1[i])