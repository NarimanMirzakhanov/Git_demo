# x = 15
# y = 25
#
# def sum_it(x, y):
#     print(f"locals {locals()}")
#     return x + y
#
#
# print(f"Inside the function: {sum_it(10, 18)}")
# print(f"Outside yhe function: {x + y}")
# print(f"Globals: {globals()}")


# name = 'Alice'
#
# def outer_function():
#     # name = 'Albert'
#     def inner_function():
#         # name = 'Alex'
#         return name
#     return inner_function
#
# closure = outer_function()
# result = closure()
#
# print(result)


# result = lambda n: n * n
# print(result(5))

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
def filter_and_sum(lst):
    new_l = []
    for x in lst:
        if isinstance(x, int):
            new_l.append(x)
    print(new_l)
    return sum(new_l)


print(filter_and_sum(list_1))

new_l = sum(filter(lambda x: isinstance(x, int), list_1))
print(new_l)

filtered = list(filter(lambda x: isinstance(x, str), list_1))
print(list(filter(lambda i: 'a' in i, filtered)))