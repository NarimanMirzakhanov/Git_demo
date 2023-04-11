# Task 2.1
import sys

# health = int(input("Input game character health: "))
# if health <= 0:
#     print(False)
# else:
#     print(True)


# Task 2.2

# num = int(input("Enter a number: "))
# if num % 2:
#     print(f"{num} is Odd number")
# else:
#     print(f"{num} is Even number")

# Task 2.3

# year = int(input("Enter a year: "))
# if not year % 4 and year != 500 and year != 600 and not year % 400:
#     print(f"{year} год является високсным")
# elif not year % 100 or year:
#     print(f"{year} год - невисокосный")


# Task 2.4

# text = input("Type any text: ")
# repeat = int(input("Enter number of repeat: "))
# print(text * repeat)


# Task 2.5

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
operator = input("Enter an operator: ")
if not num2 and operator == '/':
    print("На ноль делить нельзя")
    sys.exit()
elif operator == '/':
    result = num1 / num2
elif operator == '*':
    result = num1 * num2
elif operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
print(f"{num1} {operator} {num2} = {result}")


