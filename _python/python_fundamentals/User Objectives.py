class User:		
     def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    
     def make_deposit(self, amount):	
        self.account_balance += amount	
        return self
    
     def make_withdrawal(self, amount):
        self.account_balance -= amount	
        return self
    
     def display_user_balance(self) :
        print(f"user name :{self.name} , account balanse :{self.account_balance}") 
        return self  
    

user_1=User("ahmad","ahmad.com")
user_1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

