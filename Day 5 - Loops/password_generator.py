import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_list = []
final_password = ''

# Ask user for password length
print("Welcome to the password generator! Let's get started!")
number_letters= int(input("\nHow many letters would you like in your password?: ")) 
number_symbols = int(input("\nHow many symbols would you like?: "))
number_numbers = int(input("\nHow many numbers would you like?: "))

# Choose a random letter from the list and add it to the password list equal to the number of letters the user wants
for letter in range(1, number_letters + 1):
    password_list.append(random.choice(letters))
    
# Choose a random symbol from the list and add it to the password list equal to the number of symbols the user wants
for symbol in range(1, number_symbols + 1):
    password_list.append(random.choice(symbols))
    
# Choose a random number from the list and add it to the password list equal to the number of numbers the user wants
for number in range(1, number_numbers + 1):
    password_list.append(random.choice(numbers))

# Shuffle the password list and join it into a string
shuffled_password = random.shuffle(password_list)
final_password = ''.join(password_list)

print(f'\nYour new password is: {final_password}')