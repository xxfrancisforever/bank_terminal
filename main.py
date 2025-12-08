# from <file> import <class>
from account import Account

# pyenv local [version] in the project directory

# Arrays have mMixed data types, mutable, and ordered.
# Constants are usually written in all-caps, but it's just a readability thing
VALID_OPTIONS = [1, 2, 3, 4]

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
			if (chosen_option not in VALID_OPTIONS):
				# Would break the program if there was no "except"
				# Try to be specific when dealing with exceptions
				raise ValueError()

			return chosen_option
		# Catch a specified exception
		except ValueError:
			print("Invalid option. Choose again.")

# Sends a prompt, reads a line, converts it to a string, and returns that
# The prompt is not mandatory
user = input("How would you like to be called??\n- ")

# Prints a message to the screen
print("\nHello,", user)

current_account = Account(1, user, 100)

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
