from BankAccount import BankAccount
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(4.0)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        other_user.account.deposit(amount)
        self.account.withdraw(amount)
        return self

devon = User("Devon", "dev@gmail.com")
claire = User("Claire", "claire@gmail.com")
devon.make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance()

claire.make_deposit(50).make_deposit(100)

devon.transfer_money(claire, 75)

claire.display_user_balance()
devon.display_user_balance()