import random # Importing the random module

print("Welcome to Password Generator!") # Print a welcome message

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
 # Define the characters to be used in the password

number = input('Number of passwords? - ') # Input the number of passwords to be generated
number = int(number) # Convert the input to an integer

length = input('Password length? - ') # Input the length of the password
length = int(length) # Convert the input to an integer

print('\nHere are your passwords:') # Print a message

for pwd in range(number): # Loop through the number of passwords
    password ='' # Initialize an empty string
    for c in range(length): # Loop through the length of the password
        password += random.choice(chars) # Add a random character to the password
    print(password) # Print the password

print("\nThank you for using Password Generator!") # Print a thank you message

