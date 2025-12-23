# TODO 4: Save account logs

# from <file> import <class>
import pdb
from account import Account
from account_manager import AccountManager
from helper import ask_monetary_value

# pyenv local [version] in the project directory

# Arrays have mMixed data types, mutable, and ordered.
# Constants are usually written in all-caps, but it's just a readability thing
VALID_ACTIONS = [1, 2, 3, 4, 5]
YES_NO_OPTIONS = ['y', 'n']
MANAGER = AccountManager()

def ask_name():
	while True:
		# Sends a prompt, reads a line, converts it to a string, and returns that
		# The prompt is not mandatory
		user = input("\nHow would you like to be called?\n- ")
		
		# Checks if any character is a digit
		if not any(char.isdigit() for char in user):
			print("\nHello,", user)
			return user
		
		# Prints a message to the screen
		print("\nYour name cannot contain numbers.")

def ask_for_account():	
	while True:
		account_id = input("\nWhat's the id of the account?\n- ")

		account_found = MANAGER.retrieve_account(account_id)
		if account_found:
			return account_found	

def get_account():
	while True:
		existing = input("\nDo you already have an account with us? [y/n]\n- ")
		if existing in YES_NO_OPTIONS:
			break

	if existing == 'y':
		return ask_for_account()
	else:
		deposit_message = "How much would you like your initial deposit to be?"
		return MANAGER.add_account(ask_name(), ask_monetary_value(deposit_message))

def initialise():
	banner = """
	██▄  ▄██  ▄▄▄  ▄▄  ▄▄ ▄▄▄▄▄ ▄▄ ▄▄   ██▄  ▄██  ▄▄▄   ▄▄▄▄ ▄▄ ▄▄ ▄▄ ▄▄  ▄▄ ▄▄▄▄▄ 
	██ ▀▀ ██ ██▀██ ███▄██ ██▄▄  ▀███▀   ██ ▀▀ ██ ██▀██ ██▀▀▀ ██▄██ ██ ███▄██ ██▄▄  
	██    ██ ▀███▀ ██ ▀██ ██▄▄▄   █     ██    ██ ██▀██ ▀████ ██ ██ ██ ██ ▀██ ██▄▄▄ 
	"""
	
	print(banner)
	return get_account()

# def to declare methods
def ask_option():
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

current_account = initialise()
print("\nWelcome, ", current_account.owner)

while True:
	# Does something different for each value of the specified variable
	# Different from other programming languages, statements (if, while, etc) don't create scopes
	match ask_option():
		case 1:
			# Reassign the variable to update it
			current_account.deposit()
			current_account.show_balance()
		case 2:
			current_account.withdraw()
			current_account.show_balance()
		case 3:
			current_account.show_balance()	
		case 4:
			other_account = ask_for_account()
			current_account.transfer_to(other_account)

			current_account.show_balance()
			other_account.show_balance()
		case 5:
			print("\nGoodbye.")
			break
	
	MANAGER.save()
