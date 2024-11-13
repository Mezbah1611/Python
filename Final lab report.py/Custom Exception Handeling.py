class InsufficientFundsError(Exception):
    def __init__(self,messege):
        super().__init__(messege)
        



class BankAccount:
    
    

    def __init__(self,balance,min_balance):
        self.balance = balance
        self.min_balance = min_balance
        

    def withdraw(self,amount):
        if self.balance - amount <self.min_balance:
            raise InsufficientFundsError("Not Possible")
        
        self.balance -= amount
        print("Successfully Withdrawn")

try:
    account = BankAccount(100,20)
    account.withdraw(30)
    account.withdraw(50)
    account.withdraw(10)

except InsufficientFundsError as e:
    print("Error : ",e)