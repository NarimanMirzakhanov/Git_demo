import time


def decorator(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы программы {dt}")
        return res

    return wrapper


def square(a):
    p = a * 4
    s = a ** 2
    d = round(2 ** 0.5 * 5)
    my_tuple = (p, s, d)
    return my_tuple


square = decorator(square)

res = square(5)
print(res)
