# def my_decorator(func):
#     def wrapper(arg):
#         print("Я - обертка!")
#         func(arg)
#         print('Завернули')
#     return wrapper
#
#
# @my_decorator
# # def say_hello():
# #     print(f'Hello')
# def say_hello(name):
#     print(f"Hello, {name}")
#
#
# # say_hello = my_decorator(say_hello) # использовали @my_decorator вместо этой строки
# say_hello('Sam')

def milk(func):
    def wrapper():
        print('hot milk')
        func()

    return wrapper


def sugar(func):
    def wrapper():
        print('sugar')
        func()

    return wrapper


@sugar
@milk
def coffee():
    print('Coffee')


coffee()

