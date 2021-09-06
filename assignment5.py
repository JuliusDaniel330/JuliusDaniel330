# TWO DIFFERENT CODES WITH THE SAME ANSWER.
#      (FIRST CODE)
def is_even(num: float) -> False:
    while num >= 0:
        if num == 0:
            return True
        elif num == 1:
            return False
        num -= 2


print(is_even(5.0))

#   (SECOND CODE)


def is_even(x: int) -> True:
    return not bool(x % 2)


print(is_even(6))

