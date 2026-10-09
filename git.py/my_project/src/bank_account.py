class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than 0")
    
            if amount > self.balance:
                raise ValueError("Insufficient balance")
    
            self.balance -= amount
            print("Withdrawn:", amount)
    
    def display(self):
            print("Account Holder:", self.name)
            print("Balance:", self.balance) 

account = BankAccount("Vignesh", 1000)

try:
    account.deposit(200)
    account.withdraw(800)
    account.display()

except ValueError as e:
    print("Error:", e)            
