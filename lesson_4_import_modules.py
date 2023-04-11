import datetime
import math
from math import *
import math as m
import module
from module import hello, sum
from module import *
from module import hello as h, sum as s # переименовали функцию hello в h и sum в s

print(datetime.date.today())
# 2023-03-25
birth_year = 1983
current_date = datetime.date.today()
age = current_date.year - birth_year
current_month = current_date.month
print(age)
# 40
print(current_month)
# 3

l = [3, 5, 76, 1, -2]
print(m.prod(l))
# -2280

print(round(math.pi, 2))
# 3.14

print(m.pow(4, 2))
# 16.0

print(module.hello('Nariman'))
# Hello, Nariman

print(hello('Irina'))
# Hello, Irina
print(sum(4, 6))
# 10

print(h('Irina'))
# Hello, Irina
print(s(4, 6))
# 10