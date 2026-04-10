
class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def AtmEngine(self):
        while True:
            print("Welcome to the ATM Engine")
            print("""
            1.check balance
            2.withdrow balance
            3.deposit balance
            4. exit
            """)

            user = input("please enter your choice: ")

            if user == "1":
                print(f"your balance is {self.balance}")

            elif user == "2":
                amount = int(input("Enter the withdraw amount: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrawn: {amount}, Remaining balance: {self.balance}")
                else:
                    print("Insufficient balance!")

            elif user == "3":
                amount = int(input("Enter the deposit amount: "))
                self.balance += amount
                print(f"Deposited: {amount}, Updated balance: {self.balance}")

            elif user == "4":
                print("Thank you for using this ATM Engine")
                break
            else:
                print("enter correct input")

atm = ATM()
atm.AtmEngine()

