
for i in range(1, 21):
    print(f"{i} times table")
    print()

    for j in range(1, 13):
        print(f"{i} * {j} =", i*j)

    print()


"""
def is_even(num):
    while True:
        if num == 0:
            return True
        elif num == 1:
            return False
        num -= 2


print(is_even(6))
"""


def is_even(x: float) -> False:

    while x >= 0:
        if x == 0:
            return True
        elif x == 1:
            return False
        x -= 2


print(is_even(5.0))


def is_even(x: int) -> True:
    return not bool(x % 2)


print(is_even(6))

