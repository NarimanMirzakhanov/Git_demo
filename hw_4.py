import time
from functools import reduce
from my_calc import addition as s


# Task 4.1
def square(square_side):
    p = square_side * 4
    a = square_side ** 2
    d = square_side * round(pow(2, 0.5))
    my_tuple = (p, a, d)
    return my_tuple


print(square(5))


# Task 4.2
def employee(**kwargs):
    return kwargs


print(employee(name='John', last_name='Smith', age=35, position='web developer'))

# Task 4.3
my_list = [20, -3, 15, 2, -1, -2]

new_list = list(filter(lambda x: isinstance(x, int) and x >= 0, my_list))
print(new_list)

# # Task 4.4
result = reduce(lambda x, y: x * y, my_list)
print(result)


# Task 4.5
def name_func(mult):
    def wrapper(mult):
        start_time = time.perf_counter()
        print(start_time)
        print(f"Product of multiplication a and b is {mult(545, 525.10124)}")
        end_time = time.perf_counter()
        print(end_time)
        print(end_time - start_time)

    return wrapper(mult)


@name_func
def mult(a, b):
    return a * b


# Task 4.6
print(s(7, 8))
