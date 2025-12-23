import json
import random
from types import SimpleNamespace
from account import Account
import pdb

class AccountManager:
	def __init__(self, filename="accounts.json"):
		self.filename = filename
		self.accounts = {}

		self.load_accounts()

	def load_accounts(self):
		try:
			with open(self.filename, mode="r") as file:
				data = json.load(file)
				
				# The data is a dict, so just doing "for a in data" would give the keys
				for a in data.values():
					self.accounts[a['account_id']] = Account(
						a['account_id'],
						a['owner'],
						a['balance']
					)

		# It's better to catch exceptions instead of checking for validity
		except FileNotFoundError:
			with open(self.filename, mode="w") as file:
				# dump converts python objects to JSON format and writes them to a file
				json.dump([], file, indent=4)

		except json.JSONDecodeError:
			with open(self.filename, mode="w") as file:
				json.dump([], file, indent=4)

	def retrieve_account(self, account_id):
		try:
			return self.accounts[account_id]
		except KeyError:
			return None
	
	def save(self):
		# "w" mode creates a file if doesn't exist, and overwrites it completely
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
