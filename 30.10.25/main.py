class BankAccount:
    def __init__(self, name, y):
        self.name = name
        self.balance = y

    def print_attributes(self):
        print("Account Holder:", self.name)
        print("Initial Balance:", self.balance)
    
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
    
    def show_balance(self):
        print("Balance:", self.balance)

    def withdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Current Balance is:", self.balance)

my_acc = BankAccount("John", 10000)
my_acc.print_attributes()
my_acc.deposit(2000)
my_acc.withdrawal(3000)
my_acc.show_balance()
