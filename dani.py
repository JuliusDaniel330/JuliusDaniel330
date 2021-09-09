# Shooting Game
"""
class Enemy:
    name = ""
    lives = 0

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + ' killed')
        else:
            print(self.name + ' has ' + str(self.lives) + ' lives')


class Monster(Enemy):
    def __init__(self):
        super().__init__('Monster', 3)


class Alien(Enemy):
    def __init__(self):
        super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input("Enter please: ")
    if x == 'exit':
        break
    elif x == 'laser':
        a.hit()
    elif x == 'gun':
        m.hit()
"""
def case_count(string: str) -> dict:
  Capital = 0
  small = 0
  for char in string:
    if char.isupper():
      Capital += 1
    elif char.islower():
      small += 1
    else:
      pass

  dict = {'upper': Capital, 'lower':small}
  return dict


print(case_count("University Of Lagos"))

school = "University Of Lagos"
lowers, uppers = 0, 0
for i in school:
  if i >= 'A' and i <= 'Z':
   uppers = uppers + 1
  elif i >= 'a' and i <= 'z':
    lowers = lowers + 1


print({'upper': uppers, 'lower': lowers})


def generator(number: int) -> dict:
  dict = {}
  for i in range(number + 1):
    if i > 0:
      dict[i] = i * i
  return dict


print(generator(8))


number = int(input("Input a number: "))
direct = dict()

for x in range(1, number + 1):
    direct[x] = x*x

print(direct)

l1 = ["hello", "world", "daniel"]
for i in l1:
  print(i + "!")


list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break


def max_num(x, y):
    if x >= y:
        return x

    else:
        return y


print(max(4, 7))
z = max(8, 5)
print(z)

# Function to find average marks


def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subject = len(marks)
    average_mark = sum_of_marks / total_subject
    return average_mark

# calculate the grade and return it


def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'c'
    else:
        grade = 'F'
    return grade


marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print("your average marks is", average_marks)

grade = compute_grade(average_marks)
print("Your grade is", grade)