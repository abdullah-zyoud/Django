class BankAccount:
     def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
class User:		
     def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.account2 = BankAccount(int_rate=0.05, balance=0)
     def make_deposit(self, amount ,accountnum):	
        if (accountnum ==1):
            self.account.balance += amount 

        else :
        
               self.account2.balance += amount	

        
        return self
    
     def make_withdrawal(self, amount):
        self.account.balance -= amount	
        self.account2.balance -= amount	
        return self
    
     def display_user_balance(self) :
        print(f"user name :{self.name} , account1 balanse :{self.account.balance} account2 balanse :{self.account2.balance}") 
        return self 

user_1=User("ahmad","ahmad.com")
user_1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


print(user_1.account2.balance)