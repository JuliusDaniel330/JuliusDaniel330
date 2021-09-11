
# with dictionary comprehension
def SquareDictComp(number):
    return { i : i ** 2 for i in range(1, number + 1)}

# normal


def SquareDict(number):
    squares = {}

    for i in range(1, number + 1):
        squares[i] = i ** 2
    
    return squares

print(SquareDict(8))
print(SquareDictComp(8))