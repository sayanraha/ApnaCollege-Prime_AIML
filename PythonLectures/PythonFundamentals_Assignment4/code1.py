'''
Create  a BankAccount class with attributes account_number, owner_name and balance.
Add methods to deposit, withdraw and check balance.

'''


class BankAccount :
    
    def __init__(self, account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def Deposit(self,amount):
        self.balance += amount
        print(f"Credited {amount}/- into your Account No. {self.account_number}, available balance is {self.balance}/- ")

    def Withdraw(self,withdrawAmount):
        self.balance -= withdrawAmount
        print(f"Debited {withdrawAmount}/- from your Account No. {self.account_number}, available balance is {self.balance}/- ")

    def CheckBalance(self):
        print(f"Available balance {self.balance}/-")

obj = BankAccount("BOB1235678","Sayan Raha",10000)
print(f"Current Balance of {obj.owner_name} with Acc. No. {obj.account_number} is = {obj.balance}/- ")

obj.Deposit(20000)
obj.Withdraw(5000)
obj.CheckBalance()
