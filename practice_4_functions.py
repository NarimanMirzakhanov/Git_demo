def multi(a, b):
    return a * b


num = (multi(5, 10)) + 10
num1 = (multi(10, 10))

print(num)
print(num1)


def check_even(a):
    if a % 2 == 0:
        print(f"{i} = 'Yes'")
    else:
        print(f"{i} = 'No'")


for i in range(15):
    check_even(i)