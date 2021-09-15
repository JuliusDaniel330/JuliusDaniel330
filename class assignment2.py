
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self):
        amount = int(input("\nEnter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def bank_fees(self):
        self.balance = 95 / 100 * self.balance

    def display(self):
        print("\nAccount Name: ", self.name)
        print("\naccount number: ", self.account_number)
        print("\nAvailable Balance: ", self.balance)


Account1 = BankAccount('Julius Daniel', '19371554951', 20000)

Account1.deposit()
Account1.withdraw()
Account1.bank_fees()
Account1.display()


