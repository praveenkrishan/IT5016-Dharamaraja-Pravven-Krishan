class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
         self._balance += amount
         print(f"${amount} deposited")
        else:
           print(" deposit amount must be positive")

    def withdraw(self, amount):
       if 0 < amount <= self._balance:
          self._balance -= amount
          print(f"${amount}.withdrawn")
       else:
          print("insufficient balance or Invalid amount")

    def get_balance(self):
       return self._balance

account = Account("James", 100)

print(account.owner)

account.deposit(50)
print(account.get_balance())
account.withdraw(75)
print(account.get_balance())


                   
    