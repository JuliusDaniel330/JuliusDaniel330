"""
def stand_dev(data_set):
    # calculate average of list
    mean = sum(data_set) / len(data_set)
    # apply formula
    element_sum = 0
    for x in data_set:
        element_sum += (x-mean)**2
    variance = element_sum / len(data_set)
    # square root of variance
    std_dev = variance ** 0.5
    return std_dev


num1 = [10, 20, 30, 40, 50]
num2 = stand_dev(num1)
print(num2)


def mean(values):
    length = len(values)
    total_sum = 0

    for i in range(length):
        total_sum += int(values[1])
    total_sum = sum(values)
    average = int(total_sum * 1.0 / length)
    return average


num1 = [10, 20, 30, 40, 50]
num2 = mean(num1)
print(num2)
"""

# remove_shortest = ["lion", "animal"]


my_list = ['lion', 'goat', 'elephant', 'sheep', 'animal', 'crocodile', ]
min_list = list(filter(lambda i: len(i) == 4, my_list))

print(min_list)

my_list = ['lion', 'goat', 'elephant', 'sheep', 'animal', 'crocodile']
min_list = [x for x in my_list if len(x) == 4]


print(min_list)


def get_list(values, k):
    return [item for item in my_list if len(item) == k]


print(get_list(['lion', 'goat', 'elephant', 'sheep', 'animal', 'crocodile'], 4))