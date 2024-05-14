# You should allow customers to create a new account in our banking system.

# Once the program starts you should print the menu:

# 1. Create an account
# 2. Log into the account
# 0. Exit

# If the customer chooses ‘Create an account’, you should generate a new card number that satisfies 
# all the conditions described above. Then you should generate a PIN code that belongs to the 
# generated card number. The PIN is a sequence of 4 digits; it should be generated in the range from 0000 to 9999.

# If the customer chooses ‘Log into account’, you should ask to enter the card information.

# After the information has been entered correctly, you should allow the user to check the account balance; 
# after creating the account, the balance should be 0. 
# It should also be possible to log out of the account and exit the program.


import random

# Define a class to represent a bank account
class BankAccount:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

# Function to generate a card number
def generate_card_number():
    prefix = "400000"
    digits = "".join(str(random.randint(0, 9)) for _ in range(10))
    card_number = prefix + digits
    return card_number.ljust(16, '0')

# Function to generate a PIN
def generate_pin():
    return "{:04d}".format(random.randint(1000, 9999))

# Function to create a new account
def create_account():
    card_number = generate_card_number()
    pin = generate_pin()
    account = BankAccount(card_number, pin)
    return account

# Function to log into an account
def log_into_account(accounts):
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")
    for account in accounts:
        if account.card_number == card_number and account.pin == pin:
            return account
    return None

# Function to display the menu
def display_menu():
    print("\n1. Create an account")
    print("2. Log into account")
    print("0. Exit")

# Main program
def main():
    accounts = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            account = create_account()
            accounts.append(account)
            print("Your card has been created")
            print("Your card number: {}".format(account.card_number))
            print("Your card PIN: {}".format(account.pin))

        elif choice == '2':
            account = log_into_account(accounts)
            if account:
                print("You have successfully logged in!")
                while True:
                    print("1. Check balance")
                    print("2. Log out")
                    log_choice = input("Choose an option: ")
                    if log_choice == '1':
                        print("Balance: {}".format(account.balance))
                    elif log_choice == '2':
                        print("You have been logged out.")
                        break
            else:
                print("Wrong card details or account does not exist.")

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


