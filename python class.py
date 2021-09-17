"""
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class.
"""


class BankAccount:
    # create the constructor with parameters: accountNumber, name and balance
    def __init__(self, account_number, name, balance):
        self.accountNumber = account_number
        self.name = name
        self.balance = balance

    # create Deposit() method
    def deposit(self, d):
        self.balance = self.balance + d

    # create Withdrawal method
    def with_draw(self, w):
        if self.balance < w:
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w

    # create bankFees() method
    def bank_fees(self):
        self.balance = (95 / 100) * self.balance

    # create display() method
    def display(self):
        print("Account Number : ", self.accountNumber)
        print("Account Name : ", self.name)
        print("Account Balance : ", self.balance, "#")


# Testing the code :
newAccount = BankAccount(2178514584, "Albert", 2700)
# Creating Withdrawal Test
newAccount.deposit(30000)
# Create deposit test
newAccount.with_draw(32000)

newAccount.bank_fees()

# Display account information
newAccount.display()


class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name + " says hi")


obj = Student("John")
obj.greet()


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def the_cars(self):
        print("The", self.color, 'car has', str(self.mileage), 'miles.')


brand1 = Car("blue", '20,000')
brand1.the_cars()

brand2 = Car("red", '30,000')
brand2.the_cars()


class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\nAccount Name: ", self.name)
        print("\naccount number: ", self.account_number)
        print("\nAvailable Balance=", self.balance)


Account1 = BankAccount('Julius Daniel', '19371554951', 20000)
Account2 = BankAccount('Daniel Julius',  '19371564761', 40000)

Account1.deposit()
Account1.withdraw()
Account1.display()

Account2.deposit()
Account2.withdraw()
Account2.display()


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


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


nam = input("Enter the name: ")
lev = int(input("Enter the level: "))

P1 = Player(name, level)
P1.intro()

print(type(3))


class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")


iphone = Phone("iphone 7+", 300)
samsung = Phone("samsung s20", 1400)

print(iphone.brand)
print(iphone.price)
iphone.call("08138174405")




class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def the_cars(self):
        print("The", self.color, 'car has', str(self.mileage), 'miles.')


brand1 = Car("blue", '20,000')
brand1.the_cars()

brand2 = Car("red", '30,000')
brand2.the_cars()


class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def bank_fees(self):
        self.balance = 95 / 100 * self.balance

    def display(self):
        print("\nAccount Name: ", self.name)
        print("\naccount number: ", self.account_number)
        print("\nAvailable Balance=", self.balance)


Account1 = BankAccount('Julius Daniel', '19371554951', 20000)
Account2 = BankAccount('Daniel Julius',  '19371564761', 40000)

Account1.deposit()
Account1.withdraw()
Account1.bank_fees()
Account1.display()


Account2.deposit()
Account2.withdraw()
Account2.bank_fees()
Account2.display()


class Student:
    def __init__(self, name, marks):
        self.marks = marks
        self.name = name

    def check_pass_fail(self):
        print(f"this is mr {self.name}.")
        if self.marks >= 40:
            return True
        else:
            return False


student1 = Student("Daniel", 35)
student1.name = "Daniel"
student1.marks = 35

did_pass = student1.check_pass_fail()
print(did_pass)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def the_cars(self):
        print("The", self.color, 'car has', str(self.mileage), 'miles.')


brand1 = Car("blue", '20,000')
brand1.the_cars()

brand2 = Car("red", '30,000')
brand2.the_cars()


class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def bank_fees(self):
        self.balance = 95 / 100 * self.balance

    def display(self):
        print("\nAccount Name: ", self.name)
        print("\naccount number: ", self.account_number)
        print("\nAvailable Balance=", self.balance)


Account1 = BankAccount('Julius Daniel', '19371554951', 20000)
Account2 = BankAccount('Daniel Julius',  '19371564761', 40000)

Account1.deposit()
Account1.withdraw()
Account1.bank_fees()
Account1.display()


Account2.deposit()
Account2.withdraw()
Account2.bank_fees()
Account2.display()


class Student:
    def __init__(self, name, marks):
        self.marks = marks
        self.name = name

    def check_pass_fail(self):
        print(f"this is mr {self.name}.")
        if self.marks >= 40:
            return True
        else:
            return False


student1 = Student("Daniel", 35)
student1.name = "Daniel"
student1.marks = 35

did_pass = student1.check_pass_fail()
print(did_pass)


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return self.name + ' (' + str(self.capacity) + 'L)'

    def __add__(self, new_juice):
        return Juice(self.name + '&' + new_juice.name, self.capacity + new_juice.capacity)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        new_name = self.name+"&"+other.name
        new_capacity = self.capacity + other.capacity
        return new_name + (str(" ")) + str("(") + (str(new_capacity)+"L)")

    def __str__(self):
        return self.name + ' ('+str(self.capacity)+'L)'


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)