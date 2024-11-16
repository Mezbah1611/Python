class BankAccount:
    def __init__(self,initial_balance = 0):
        self.__balance = initial_balance

    
    def Deposit(self,ammount):
        self.__balance += ammount 
        print('Deposit Seccessful') 
        

    def Withdraw(self,ammunt):
        if ammunt < self.__balance:
            self.__balance -= ammunt
            print('Withdraw succesful,New Balance :',self.__balance)

        else:
            print('Withdrawal amount exceeds current balance')
        

    def CheckBalance(self):
        return self.__balance
    

account = BankAccount(initial_balance= 100)
account.Deposit(50)
account.Withdraw(200)
account.Withdraw(20)
        