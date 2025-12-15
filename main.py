class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        self.balance -= amount

    def __str__(self):
        return f'{self.owner} balance: {self.balance}'


account = BankAccount('Ali')
account.deposit(1000)
print(account)
print(account.withdraw(1500))
account.withdraw(300)
print(account)
