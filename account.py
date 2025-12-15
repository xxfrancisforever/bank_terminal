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
		print("\nCurrent balance: €{:.2f}".format(self.balance))

	def deposit(self):
		while True:
			try:
				self.balance += float(input("\nHow much would you like to deposit?\n- "))
				break
			except ValueError:
				print("Invalid input.")

	def withdraw(self):
		while True:
			try:
				withdraw_value = float(input("\nHow much would you like to withdraw?\n- "))
				break;
			except ValueError:
				print("Invalid input.")
		
		if (self.balance - withdraw_value < 0):
			print("\nYou don't have enough balance to complete this action")
			return
		else:
			# For the variable to change outside of the function, return the new value
			self.balance -= withdraw_value	
