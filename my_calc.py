def addition(a, b):
    return a + b


def extraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if not b:
        return "На ноль делить нельзя"
    else:
        return a / b