class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdaraw(self, amount):
        self.balance -= amount
        print("통장에서", amount, "가 출금되었음 ")
        print("잔액:",self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("통장에서", amount, "가 입금되었음 ")
        print("잔액:",self.balance)


a = BankAccount()
a.deposit(100)
a.withdaraw(10)