# mult = lambda x, y: x*y
# print(mult(5, 6))


l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, l))
print(filtered)
# [20, 18, 48]
# power = list(map(lambda x: x**2 if isinstance(x, int) else l.remove(x), l))

power = list(map(lambda x: x ** 2 if isinstance(x, int) else x, l))
print(power)
# [400, 'str', 225, 324, 'yes', 'apple', 2304, 40.5]

l1 = [20, 15, 8, 7, 6]
power1 = list(map(lambda x: x ** 2, l1))
print(power1)
# [400, 225, 64, 49, 36]

from functools import reduce

result = reduce(lambda x, y: x * y, l1)
print(result)
# 100800
