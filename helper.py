def ask_monetary_value(message):
	while True:
		try:
			# The name of a value type can be used to convert to it
			return float(input("\n" + message + "\n- " ))
		except ValueError:
			print("\nInvalid value.")
