# NO 2 WITH A Defined function called square_dict.
def square_dict(number: int) -> dict:
  dict = {}
  for i in range(number + 1):
    if i > 0:
      dict[i] = i * i
  return dict


print(square_dict(8))

# With an input function for the user to input an integer value.
number = int(input("Input a number: "))
direct = {}

for x in range(1, number + 1):
    direct[x] = x*x

print(direct)
