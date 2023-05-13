class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
    	self.account_balance += amount	
    def make_withdrawal(self, amount):
        self.account_balance -= amount	
    def display_user_balance(self) :
        print(f"user name :{self.name} , account balanse :{self.account_balance}")   
    def transfer_money(self, other_user, amount):
        
        pass

user_1=User("ahmad","ahmad.com")
user_1.make_deposit(1000)
print(user_1.account_balance)
user_1.make_withdrawal(500)
print(user_1.name)
print(user_1.account_balance)
user_1.display_user_balance()
