import math

my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x > 0, my_list)))
print(math.prod(filter(lambda x: x, my_list)))