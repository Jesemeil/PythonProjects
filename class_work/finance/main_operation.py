from account import Account
from bank import Bank
import account_test
import bank_test


def main():
    print("Welcome to the Banking Application!")

    bank = Bank()

    while True:
        print("\nMain Menu:")
        print("1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Exit Application")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            pin = input("Enter your PIN: ")
            bank.register(first_name, last_name, pin)
            print("Account successfully opened!")

        elif choice == "2":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter the amount to deposit: "))
            bank.deposit(amount, account_number)
            print("Deposit successful!")

        elif choice == "3":
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            amount = float(input("Enter the amount to withdraw: "))
            bank.withdraw(amount, account_number, pin)
            print("Withdrawal successful!")

        elif choice == "4":
            from_account_number = input("Enter your account number: ")
            from_pin = input("Enter your PIN: ")
            to_account_number = input("Enter the recipient's account number: ")
            amount = float(input("Enter the amount to transfer: "))
            bank.transfer(amount, from_account_number, to_account_number, from_pin)
            print("Transfer successful!")

        elif choice == "5":
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            balance = bank.check_balance(account_number, pin)
            print(f"Your balance: {balance}")

        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
