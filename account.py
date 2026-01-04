import pdb

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

	def deposit(self, value):	
		if value <= 0:
			return None

		self.balance += value
		return value

	def withdraw(self, value):
		if (self.balance - value < 0):
			return None
		else:
			# For the variable to change outside of the function, return the new value
			self.balance -= value	
			return value

	def transfer_to(self, other_account, value):
		if value > self.balance:
			return None
		
		self.balance -= value
		other_account.balance += value

		return value
