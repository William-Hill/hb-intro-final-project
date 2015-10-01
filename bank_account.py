class Bank_Account(object):
	def __init__(self,name,account_balance):
		self.name = name
		self.account_balance = account_balance
	def deposit(self, money_deposited):
		self.account_balance += money_deposited
	def withdraw(self,money_withdrawn):
		self.account_balance -= money_withdrawn

my_account = Bank_Account("William", 10)
