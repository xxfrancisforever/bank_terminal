import pdb
from helper import ask_monetary_value

NOT_ENOUGH_MONEY = "\nYou don't have enough balance to complete this action"

# class to declare a class
class Account:
	#Constructor, pass self as first argument
	def __init__(self, account_id, owner, balance):
		# The id needs to be generated outside because it requires all the previous accounts
		self.account_id = account_id

		self.owner = owner
		self.balance = balance
		
	# Pass self as the first argument for instance methods
	def show_balance(self):
		# self has the attributes of an object
		print("\nBalance for {}: €{:.2f}".format(self.account_id, self.balance))

	def deposit(self):
		message = "How much would you like to deposit?"
		self.balance += ask_monetary_value(message)

	def withdraw(self):
		message = "How much would you like to withdraw?"
		withdraw_value = ask_monetary_value(message)	
	
		if (self.balance - withdraw_value < 0):
			print(NOT_ENOUGH_MONEY)
			return
		else:
			# For the variable to change outside of the function, return the new value
			self.balance -= withdraw_value	

	def transfer_to(self, other_account):
		message = "How much would you like to transfer?"
		transfer_value = ask_monetary_value(message)

		if transfer_value  > self.balance:
			print(NOT_ENOUGH_MONEY)
			return
		
		self.balance -= transfer_value
		other_account.balance += transfer_value
