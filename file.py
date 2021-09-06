"""
x = input("Enter your three characters:")
print(x[0:3])

best_footballer = input("Who is the best footballer in the world?: ")

if best_footballer == 'ronaldo':
    print("The 'if' block is running")
    print("yes! you got that right")
    print("Ronaldo is the goat")

    club = input("What club is ronaldo? ")

    if club == 'juventus':
        print("yes he is a juventus player")

print("Done")
print("The program has finished executing")




print("This program checks if you are allowed to watch a horror movie\n")
print()
age = int(input("How old are you: "))

if  age >= 18:
    print("yes you are allowed")
else:
    if age >= 13:
        print("You  must come along with your parents")

    else:
        if age >= 9:
            print("there is a kiddies section meant for you")
        else:
            print("you are not allowed")






print("This is the second implementation with elif")
age = int(input("how old are you: "))

if age >= 18:
    print("yes you are allowed")
elif age >= 13:
    print("You must come along with your parents")
elif age >= 9:
    print("there is a kiddies section meant for you")
else:
    print("You are not allowed")



best_footballer = input("Whos is the best footballer in the world? ")

if best_footballer == 'ronaldo':
    print("yes! you got that right")
    print("Ronaldo is the goat")

    club = input("What club is ronaldo? ")

    if club == 'juventus':
        print("yes he is a juventus player")
    elif club == "madrid":
        print("That is his old club")
    else:
        print("you got it wrong. It's juventus")
elif best_footballer == 'messi':
    print("Ronaldo is better than messi by far")
else:
    print("Are you joking here?!!")



N = int(input("Enter your sum:"))
sum = 0
x = range(1,N+1)
for i in x:
    sum += i
    print(i)
print(sum)




bill = int(input("Enter your bill:" ))
cost = bill * (20 / 100)
print(float(cost))




weight = int(input("Enter your weight BMI:"))
height = float(input("Enter your height BMI:"))
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi > 25 and bmi < 30:
    print("Overweight")
elif bmi > 30 and bmi > 35:
    print("Obesity")
else:
    pass



nums = [1, 2, 3]
nums.append(4)
print(nums)


nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)



text = input("Enter this:")
word = input("Enter a word:")
def search(text, word):
    if word in text:
        print("word found")
    else:
        print("word not found")

search(text, word)
"""

"""
print((True and True) and (True == False))


fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

key = input("enter your country freedom rank, please:")
print(data.get(key, "not found"))









contact = [
    ("James", 42),
    ("Amy", 24),
    ("John", 31),
    ("Amanda", 63),
    ("Bab", 18)
 ]
name = input("Enter your name please:")
for x in contact:
    if name in x:
        print(str(x[0]) + " is " + str(x[1]))
        break
    else:
        print("Not found")
        break
        
        
def calc(x):
    p = side * 4
    a = side * side
    return p,a


side = int(input("Enter your number:"))
p,a = calc(side)

print("perimeter: " + str(p))
print("area: " + str(a))



skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(','.join(skills & job_skills))



#skill = input("enter skill:")
#for x in skills & job_skills:
    #if skill in x:
        #print("matched")
    #else:
        #pass


count = 1
while True:
    print(f'{count}. forever')

    count += 1

    if count > 5:
        print("stopping the loop now")
        break

while True:
    name = input("please type 'your name': ")

    if  name == 'your name':
        break


print("thank you")



while True:
    name = input("Enter your username: ")

    if name != 'Daniel':
        print("wrong password")
        continue

    print(f'Hello, {name}. what is your password?')

    while True:

        password = input("Enter your password: ")
        if password != 'nigeria':
            print('wrong password')
            continue
        else:
            break

    if password == 'nigeria':
        break

print('Access granted')

for i in range(1, 6):
    print(f'{i} times table')
    print()

    for j in range(1,13):
        print(f'{i} * {j}')

    print()


text = input("Enter text:")
dict = {}

for i in text:
    dict[i] = text.count(i)

print(dict)
"""
"""
price = int(input("Enter the price: "))
percentage = int(input("Enter your percentage: "))

res = (lambda x, y: x*y/100)(price, percentage)
print(res)

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
def add_bonus(x):
    return x + bonus

result = list(map(add_bonus, salaries))


print(result)

def add(salary):

    return salary + bonus


salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
result = list(map(add, salaries))
print(result)


def greet(name, title):
    print("Hello")
    print("Good day")
    print(f"Nice to meet you, {title}.{name}")


greet('Julius', 'Mr')

def calculateTotal(price, quantity):

    total = price * quantity

    return total


print(calculateTotal(500, 34))

eggsTotal = calculateTotal(70, 60)
breadTotal = calculateTotal(500, 3)
onions = calculateTotal(30, 15)


print("eggsTotal:", eggsTotal)
print("breadTotal:", breadTotal)
print('onions:', onions)

print(calculateTotal(70, 50))
"""




"""


def animals(ages):
    return


number = int(input())
ages = [3, 1, 9, 0.4, 7, 12, 2, 1.7, 5.7, 42, 6.7, 14.5, 21]
older = list(filter(lambda x: x > number, ages))
print(len(older))


ages = [3, 1, 9, 0.4, 7, 12, 2, 1.7, 5.7, 42, 6.7, 14.5, 21]
a = int(input())
result = len(list(filter(lambda x: x > a, ages)))
print(result)



def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word


print(list(make_word()))
"""
"""
def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)


print(fib(4))
"""
"""
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = list(filter(lambda x: x > 1, nums))
print(nums)


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y -1)


print(power(2, 3))
"""

"""
while True:
    length = float(input("Enter the length: "))
    breath = float(input("Enter the breath: "))
    height = float(input("Enter the height: "))

    volume = length * breath * height
    print("Volume: ", volume, "cm")
    print("Do you want to perform another computation?")
    response = input("enter 'yes' or 'y' to continue, enter 'no' or n to quit: ")

    if response == 'yes' or response == 'y':
        continue
    else:
        break




def bacon():
    global name
    print (name*2)
    name = "Mike"
    eggs = 100
    print(eggs)



def spam():
    eggs = 50
    bacon()
    print(eggs)


spam()
"""
"""
x = 1
while x <= 10:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is ood")
    x += 1
"""

"""
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


nam = input("Enter the name: ")
lev = int(input("Enter the level: "))

P1 = Player("Daniel")

print(type(3))
"""

"""
def find(num):
    num_type = "odd"   # code logic here
    if num % 2 == 0:
        num_type = "even"
    return num_type


num = int(input('Enter the number: '))
num_type = find(num)

print('Given number is', num_type)


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


name = input("Enter the name: ")
level = (input("Enter the level: "))

jo = Player(name, level)
jo.intro()



# How would the attribute __a of the class b be accessed from outside the class?


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
    x = input("Enter your input: ")
    if x == 'exit':
        break
    elif x == 'laser':
        a.hit()
    elif x == 'gun':
        m.hit()


try:
    name = input("Enter: ")
    if len(name) < 4:
        raise NameError

except:
    print("Invalid Name")

else:
    print("Account Created")
"""


x = 4
y = 2
if not 1 + 1 == y or x == 4 and 8 == 8:
    print("Yes")
elif x > y:
  print("No")

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
print(nums)


items = [42, 88, 721, 12, 43, 22, 908]
num = int(input("Enter num: "))
if num in items:
    print("bingo")


def remove_longer(words: list, max_length: int):

    result = []

    for word in words:
        if len(word) < max_length:
            result.append(word)

    return result


print(remove_longer(["lion", "elephant", "goat"], 4))



nums = [9, 8, 7, 6, 5]
#nums.append(4)
nums.insert(2)
print(len(nums))

words = ["python", "fun"]
index = 1
words.insert(index, "is")
print(words)