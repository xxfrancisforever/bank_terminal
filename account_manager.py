import json
import random
from types import SimpleNamespace
from account import Account

class AccountManager:
	def __init__(self, filename="accounts.json"):
		self.filename = filename
		self.accounts = {}

	def load_accounts(self):
		# with ensures a resource is cleaned after use
		# mode "r" is for read-only
		with open(self.filename, mode="r") as file:
			data = json.load(file)
			for a in data:
				print(a)
	
	def save(self):
		with open(self.filename, mode="w") as file:
			# json can't serialise an object, turn into dict			
			# o.__dict__ makes a dict out of the object attributes, ALL included
			# lambda is a short and anonymous function. Syntax:
			# lambda [params]: [return value]
			json.dump(
				self.accounts,
				file,
				default=lambda o: o.__dict__, 
				indent=4
			)

	def add_account(self, owner, balance):
		while True:
			# random.choices returns a LIST with len=k, filled with random values you defined
			# ''.join makes a string out of the list the choices generated
			new_id = ''.join(random.choices('0123456789', k=8))
			if new_id not in self.accounts:
				# walrus operator doesn't work with class attributes/dict keys
				self.accounts[new_id] = Account(new_id, owner, balance)
				self.save()

				return self.accounts[new_id]
