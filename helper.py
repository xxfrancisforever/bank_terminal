def ask_float(message):
	while True:
		try:
			# The name of a value type can be used to convert to it
			return float(input("\n" + message + "\n- " ))
		except ValueError:
			print("\nInvalid value.")

def ask_digitless_string(message):
	while True:
		try:
			# Sends a prompt, reads a line, converts it to a string, and returns that
			# The prompt is not mandatory
			user_input = input("\n" + message + "\n - ")
			if any(char.isdigit() for char in user_input):
				raise ValueError

			return user_input	
		except ValueError:	
			# Prints a message to the screen
			print("\nYour name cannot contain numbers.")

def ask_option(message, options):
	while True:
		try:
			user_input = input("\n" + message + "\n- ").upper()
			if user_input not in options:
				raise ValueError

			return user_input
		except ValueError:
			print("Invalid option. Choose again.")
