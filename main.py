# Imports
from random import randint, shuffle
from data import letters, symbols, numbers

print("Welcome to the PyPassword Generator.")
# Prompt user for number of letters, symbols, and numbers:
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
# Create strings to store chosen letters, symbols, and numbers:
chosen_letters = ""
chosen_symbols = ""
chosen_numbers = ""
# Iterate through letters list as many times as nr_letters.
# Generate a random index each time and add letters[index] to chosen_letters:
for letter in range(nr_letters):
    index = randint(0, len(letters) - 1)
    chosen_letters += letters[index]
# Iterate through symbols list as many times as nr_symbols.
# Generate a random index each time and add symbols[index] to chosen_symbols:
for symbol in range(nr_symbols):
    index = randint(0, len(symbols) - 1)
    chosen_symbols += symbols[index]
# Iterate through numbers list as many times as nr_numbers.
# Generate a random index each time and add numbers[index] to chosen_numbers:
for number in range(nr_numbers):
    index = randint(0, len(numbers) - 1)
    chosen_numbers += numbers[index]
# Return a concatenation of chosen_letters, chosen_symbols, chosen_strings:
simplepassword = chosen_letters + chosen_symbols + chosen_numbers
print(f"Your simple secure password is: {simplepassword}")
# Cast simple password to a list, shuffle the list, and rejoin to create a complex password:
password_list = list(simplepassword)
shuffle(password_list)
complex_password = "".join(password_list)
print(f"Your more secure shuffled password is: {complex_password}")

