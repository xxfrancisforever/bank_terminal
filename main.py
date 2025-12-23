# TODO 2: Saving after every action
# TODO 3: Transfer money by account id

# from <file> import <class>
import pdb
from account import Account
from account_manager import AccountManager

# pyenv local [version] in the project directory

# Arrays have mMixed data types, mutable, and ordered.
# Constants are usually written in all-caps, but it's just a readability thing
VALID_ACTIONS = [1, 2, 3, 4]
YES_NO_OPTIONS = ['y', 'n']
MANAGER = AccountManager()

def ask_name():
	while True:
		# Sends a prompt, reads a line, converts it to a string, and returns that
		# The prompt is not mandatory
		user = input("How would you like to be called?\n- ")

		if not any(char.isdigit() for char in user):
			print("\nHello,", user)
			return user
		
		# Prints a message to the screen
		print("\nYour name cannot contain numbers.")

def ask_balance():
	while True:
		try:
			return float(input("How much will be your initial deposit?\n- "))
		except ValueError:
			print("\nInvalid value.")

def get_account():
	while True:
		existing = input("\nDo you already have an account with us? [y/n]\n- ")
		if existing in YES_NO_OPTIONS:
			break

	if existing == 'y':
		while True:
			account_id = input("\nWhat's your account id?\n- ")

			account_found = MANAGER.retrieve_account(account_id)
			if account_found:
				return account_found	
	else:
		return MANAGER.add_account(ask_name(), ask_balance())

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
		try:
			# The strings are concatenated with \n separating them
			print("\n1. Deposit", "2. Withdraw", "3. Get balance", "4. Exit", sep="\n")

			# The input is converted to an int
			chosen_option = int(input("\nOption: "))
			
			# Check if value is inside the array
			if chosen_option not in VALID_ACTIONS:
				# Would break the program if there was no "except"
				# Try to be specific when dealing with exceptions
				raise ValueError()

			return chosen_option
		# Catch a specified exception
		except ValueError:
			print("Invalid option. Choose again.")

current_account = initialise()
print("Welcome, ", current_account.owner)

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
			print("\nGoodbye.")
			break
