class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
       return f"Owner: {self.owner} | Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Otillräckligt saldo!")
        else:
            self.balance -= amount

    def show_balance(self):
        return f"{self.owner}s current balance is {self.balance}"
    
    def transfer_to(self, other_account, amount: int):
        if amount > self.balance:
            print("Otillräckligt saldo")
        else:
            self.balance -= amount
            other_account.balance += amount
            return self.balance
            

p1 = BankAccount("Alexander", 500)
p2 = BankAccount("Vincent", 300)
print()
print(p1.show_balance())
print(p2.show_balance())

p1.transfer_to(p2, 500)

print(p1.show_balance())
print(p2.show_balance())

p2.transfer_to(p1, 700)
print()
print(p1.show_balance())
print(p2.show_balance())

