#  Create a file with the User class, including the __init__ and make_deposit methods
class User:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0.00		

    def make_deposit(self,amount):
        self.account_balance += amount


#  Add a make_withdrawal method to the User class
    def make_withdraw(self, amount):
        self.account_balance -= amount

#  Add a display_user_balance method to the User class
    def display_user_balance(self):
        print('User:' + self.name + ', Balance: $' + str(self.account_balance))

    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

#  Create 3 instances of the User class
Cap_America= User ("Steve Rogers", "srogers@avengers.com")
ironman = User ("Tony Starks", "tstarks@starksenterprises.com")
Black_Widow = User ("Natasha Romanova", "nromanova@avengers.com")

#  Have the first user make 3 deposits and 1 withdrawal and then display their balance
Cap_America.make_deposit(500)
Cap_America.make_deposit(200)
Cap_America.make_deposit(200)
Cap_America.make_withdraw(150)
Cap_America.display_user_balance()

#  Have the second user make 2 deposits and 2 withdrawals and then display their balance
ironman.make_deposit(500)
ironman.make_deposit(600)
ironman.make_withdraw(200)
ironman.make_withdraw(300)
ironman.display_user_balance()

#  Have the third user make 1 deposits and 3 withdrawals and then display their balance
Black_Widow.make_deposit(900)
Black_Widow.make_withdraw(50)
Black_Widow.make_withdraw(100)
Black_Widow.make_withdraw(100)
Black_Widow.display_user_balance()

#  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
Cap_America.transfer_money(Black_Widow, 150)
Cap_America.display_user_balance()
Black_Widow.display_user_balance()


