class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError ("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insuffecient funds")
        self.balance -= amount
        return self.balance

    def display(self):
        return f"Account Holder:{self.account_holder} and balnce is:{self.balance}"



account = BankAccount("Chandu", 5000)
account.deposit(5000)
account.withdraw(2000)
final = account.display()
print(final)