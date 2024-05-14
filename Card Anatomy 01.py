# You should allow customers to create a new account in our banking system.

# Once the program starts, you should print the menu:

# 1. Create an account
# 2. Log into account
# 0. Exit

# If the customer chooses ‘Create an account’, you should generate a new card number which satisfies all the 
# conditions described above. Then you should generate a PIN code that belongs to the generated card number. 
# The PIN code is a sequence of any 4 digits. PIN should be generated in a range from 0000 to 9999.

# If the customer chooses ‘Log into account’, you should ask them to enter their card information. 
# Your program should store all generated data until it is terminated so that a user is able to log 
# into any of the created accounts by a card number and its pin. You can use an array to store the information.

# After all information is entered correctly, you should allow the user to check the account balance; 
# right after creating the account, the balance should be 0. It should also be possible to log out 
# of the account and exit the program.


import random

# Initialize an empty list to store account information
accounts = []

def generate_card_number():
    # Generate a random 16-digit card number
    return "".join(str(random.randint(0, 9)) for _ in range(16))

def generate_pin():
    # Generate a random 4-digit PIN
    return "".join(str(random.randint(0, 9)) for _ in range(4))

def create_account():
    # Generate a new card number and PIN
    card_number = generate_card_number()
    pin = generate_pin()
    # Add the new account to the list of accounts
    accounts.append({"card_number": card_number, "pin": pin, "balance": 0})
    print(f"Your new card number is: {card_number}")
    print(f"Your new PIN is: {pin}")

def login():
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")
    # Check if the card number and PIN are valid
    for account in accounts:
        if account["card_number"] == card_number and account["pin"] == pin:
            print("Login successful!")
            # Allow the user to check their account balance
            print(f"Your account balance is: {account['balance']}")
            break
    else:
        print("Invalid card number or PIN.")

def main():
    while True:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()