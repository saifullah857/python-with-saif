# 1 - BankAccount
class BankAccount:
    def __init__(self , account_no ,owner_name , balance ):
        self.account_no = account_no
        self.owner_name = owner_name
        self.balance = balance
        
    def deposit(self , amount):
        self.balance += amount
        print(f"Amount deposited = {amount}")
        print(f"Balance after deposit = {self.balance}")
        