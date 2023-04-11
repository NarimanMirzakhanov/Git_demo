# def fun(x):
#     if x <= 10:
#         print(x)
#         fun(x + 1)
#
#
# fun(1)

# Factorial
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(5))


# Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
