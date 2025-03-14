
account_numbers = []
names = []
addresses = []
balances = []
emails = []
phones = []
passwords = []




def get_valid_string(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            print("Please enter a valid string.")
        else:
            return value




def create_account():
    try:
        name = get_valid_string("\nEnter your name: ")
        address = get_valid_string("Enter your address: ")
        email = get_valid_string("Enter your email: ")
        phone = input("Enter your phone number: ")
        deposit_amount = int(input("Enter your deposit amount: "))
        while True:
            password = input("Enter your new password: ")
            confirmed_password = input("Confirm your password: ")
            if password == confirmed_password:
                break
            else:
                print("Passwords do not match. Try again.")
        
        account_number = len(account_numbers) + 1

        account_numbers.append(account_number)
        names.append(name)
        addresses.append(address)
        emails.append(email)
        phones.append(phone)
        passwords.append(password)
        balances.append(deposit_amount)

        print("\nAccount created successfully. Your account number is:", account_number)
    except ValueError:
        print("\nPlease enter a valid integer for the deposit amount.")
    except Exception as e:
        print("\nAn error occurred: ", str(e))





def deposit():
    try:
        account_number = int(input("\nEnter your account number: "))
        if account_number not in account_numbers:
            print("Your account is not created. Please create your account first.")
            return
        password = input("Enter your password: ")

        for i in range(len(account_numbers)):
            if account_numbers[i] == account_number and passwords[i] == password:
                print("Your current balance is: ", balances[i])
                deposit_amount = int(input("Enter the amount you want to deposit: "))
                balances[i] += deposit_amount
                print("Your new balance is: ", balances[i])
                return
        print("\nInvalid account number or password")
    except ValueError:
        print("\nPlease enter a valid integer for the account number or deposit amount.")





def withdraw():
    try:
        account_number = int(input("\nEnter your account number: "))
        if account_number not in account_numbers:
            print("Your account is not created. Please create your account first.")
            return
        password = input("Enter your password: ")

        for i in range(len(account_numbers)):
            if account_numbers[i] == account_number and passwords[i] == password:
                print("Your current balance is: ", balances[i])
                withdraw_amount = int(input("Enter the amount you want to withdraw: "))
                if balances[i] >= withdraw_amount:
                    balances[i] -= withdraw_amount
                    print(f"Withdrawal amount is {withdraw_amount}, and new balance is {balances[i]}")
                else:
                    print("Insufficient balance")
                return
        print("\nInvalid account number or password")
    except ValueError:
        print("\nPlease enter a valid integer for the account number or withdrawal amount.")





def check_balance():
    try:
        account_number = int(input("\nEnter your account number: "))
        if account_number not in account_numbers:
            print("Your account is not created. Please create your account first.")
            return
        password = input("Enter your password: ")

        for i in range(len(account_numbers)):
            if account_numbers[i] == account_number and passwords[i] == password:
                print("Your current balance is: ", balances[i])
                return
        print("\nInvalid account number or password")
    except ValueError:
        print("\nPlease enter a valid integer for the account number.")



def exit_program():
    print("\nThanks for using our services")



def main():
    while True:
        print("<<<< Welcome to the bank >>>>")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                create_account()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                check_balance()
            elif choice == 5:
                exit_program()
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid integer for your choice.")



if __name__ == "__main__":
    main()
