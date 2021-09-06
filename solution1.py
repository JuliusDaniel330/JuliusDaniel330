from math import sqrt

def CreateList(amount: int) -> list:
    values = []

    for i in range(amount):
        number = float(input("Enter a value: "))
        values.append(number)

    return values


def ComputeMeanStd(values: list):

    # total = 0
    # for number in values:
    #     total += number
    # mean = total / len(values)

    mean = sum(values) / len(values)

    total = 0

    for number in values:
        total += ((number - mean) ** 2)

    variance = total / len(values)

    std = sqrt(variance)

    print("Mean:", mean)
    print("Std:", std)



ComputeMeanStd(CreateList(5))