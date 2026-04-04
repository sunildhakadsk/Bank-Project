class BankAcc:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def credit_money(self, amount):
        self.balance += amount
        print(f"my bank balance {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"my bank balance {self.balance}")

    def __str__(self):
        return f"{self.owner}: ₹{self.balance}"
    
Acc = BankAcc("Sunil",1000)

while True:

    print(""" Wellcome To My Bank
    1. Credit Payment
    2. Withdraw Payment
    3. Check Balance
    """)

    user = int(input("Choose option: "))

    if user == 1:
        amount = int(input("Enter amount to credit: "))
        if Acc.credit_money(amount):
            print("Money Credited")

    elif user == 2:
        amount = int(input("Enter amount to withdraw: "))
        if Acc.withdraw(amount):
            print("withdraw your money")

    elif user == 3:
        print(f"Owner: {Acc.owner} Balance: {Acc.balance}")

    else:
        print("error")

print(Acc)

