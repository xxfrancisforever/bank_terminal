# TODO 4: Save account logs


# from <file> import <class>
import pdb
from account import Account
from account_manager import AccountManager
from helper import *

# pyenv local [version] in the project directory

# Arrays have mMixed data types, mutable, and ordered.
# Constants are usually written in all-caps, but it's just a readability thing
VALID_ACTIONS = [1, 2, 3, 4, 5]
YES_NO_OPTIONS = ['Y', 'N']
MESSAGES = {
	'NOT_ENOUGH_MONEY': "\nYou don't have enough balance to complete this action",
	'deposit': "How much would you like to deposit?",
	'withdraw': "How much would you like to withdraw?",
	'transfer': "How much would you like to transfer?"
}
MANAGER = AccountManager()

# def to declare methods
def ask_action():
	# Runs until a break statement
	while True:
		# The strings are concatenated with \n separating them
		print("\n1. Deposit", "2. Withdraw", "3. Get balance", "4. Transfer",  "5. Exit", sep="\n")

		# The input is converted to an int
		chosen_option = int(input("\nOption: "))
		
		# Check if value is inside the array
		if chosen_option in VALID_ACTIONS:
			return chosen_option

		print("Invalid option. Choose again.")

def ask_for_account():	
	while True:
		account_id = input("\nWhat's the id of the account?\n- ")

		account_found = MANAGER.retrieve_account(account_id)
		if account_found:
			return account_found	

def get_account():
	yes_no_message = "Do you already have an account with us? [y/n]"
	existing = ask_option(yes_no_message, YES_NO_OPTIONS)

	if existing == 'Y':
		return ask_for_account()
	else:
		deposit_message = "How much would you like your initial deposit to be?"
		name_message = "How would you like to be called?"

		return MANAGER.add_account(ask_digitless_string(name_message), ask_float(deposit_message))

def initialise():
	banner = """
	██▄  ▄██  ▄▄▄  ▄▄  ▄▄ ▄▄▄▄▄ ▄▄ ▄▄   ██▄  ▄██  ▄▄▄   ▄▄▄▄ ▄▄ ▄▄ ▄▄ ▄▄  ▄▄ ▄▄▄▄▄ 
	██ ▀▀ ██ ██▀██ ███▄██ ██▄▄  ▀███▀   ██ ▀▀ ██ ██▀██ ██▀▀▀ ██▄██ ██ ███▄██ ██▄▄  
	██    ██ ▀███▀ ██ ▀██ ██▄▄▄   █     ██    ██ ██▀██ ▀████ ██ ██ ██ ██ ▀██ ██▄▄▄ 
	"""
	
	print(banner)
	return get_account()

current_account = initialise()
print("\nWelcome, ", current_account.owner)

while True:
	# Does something different for each value of the specified variable
	# Different from other programming languages, statements (if, while, etc) don't create scopes
	match ask_action():
		case 1:
			current_account.deposit(ask_float(MESSAGES['deposit']))
		case 2:
			current_account.withdraw(ask_float(MESSAGES['withdraw'])) 
		case 3:
			current_account.show_balance()	
		case 4:
			other_account = ask_for_account()
			current_account.transfer_to(other_account, ask_float(MESSAGES['transfer']))
		case 5:
			print("\nGoodbye.")
			break
	
	MANAGER.save()
