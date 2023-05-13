class BankAccount:
     def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        

     def deposit(self, amount):
        self.balance+=amount
        return self
        
     def withdraw(self, amount):
        if self.balance>5:
             self.balance-=amount
        else:
             print( "Insufficient funds: Charging a $5 fee")
        return self

     def display_account_info(self):
        print(f"Balance:  :{self.balance} ") 
        return self

     def yield_interest(self):
        self.balance-=self.balance*self.int_rate
        print(f"Balance:  :{self.balance} ")
        return self

account_1=BankAccount(0.05,1500)
account_2=BankAccount(0.03,2500)
account_1.deposit(500).deposit(400).deposit(200).withdraw(200).display_account_info().yield_interest()
account_2.deposit(200).deposit(900).withdraw(100).withdraw(500).withdraw(100).withdraw(50).display_account_info().yield_interest()

