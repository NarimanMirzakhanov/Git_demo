import sys

try:
    num1 = int(input('Number 1: '))
    num2 = int(input('Number 2: '))
except ValueError:
    print("Вы ввели не число")
    sys.exit()
operator = input('Operator: ')
if (num2 == 0 and operator == '/') or num1 > 5:
    try:
        result = num1 / num2
        print(f"Result = {result}")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
else:
    result = num1 * num2
    print(f"Result = {result}")