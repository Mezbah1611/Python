class InsufficientFunds(Exception):
    def __init__(self,messege = "Insufficent funds in the account") :
        self.messege = messege
        super().__init__(self.messege)
        
class BankAccount:
    def __init__(self,balance) :
        self.balance = balance
        
    def withdraw(self,ammount):
        try:
            if ammount > self.balance:
                raise InsufficientFunds("Withdrawl ammount exceeds balance")
            else:
                self.balance -= ammount
                print("Successful")
        except InsufficientFunds as e:
            print("Error",e)
acc = BankAccount(500)
acc.withdraw(10000)