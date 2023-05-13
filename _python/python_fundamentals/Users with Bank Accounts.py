class BankAccount:
     def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        

    #  def deposit(self, amount):
    #     self.balance+=amount
    #     return self
        
    #  def withdraw(self, amount):
    #     if self.balance>5:
    #          self.balance-=amount
    #     else:
    #          print( "Insufficient funds: Charging a $5 fee")
    #     return self

    #  def display_account_info(self):
    #     print(f"Balance:  :{self.balance} ") 
    #     return self

    #  def yield_interest(self):
    #     self.balance-=self.balance*self.int_rate
    #     print(f"Balance:  :{self.balance} ")
    #     return self

class User:		
     def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
     def make_deposit(self, amount):	
        self.account.balance += amount	
        return self
    
     def make_withdrawal(self, amount):
        self.account.balance -= amount	
        return self
    
     def display_user_balance(self) :
        print(f"user name :{self.name} , account balanse :{self.account.balance}") 
        return self 

user_1=User("ahmad","ahmad.com")
user_1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()