from account import Account, CustomError


class Bank:
    def __init__(self):
        self.accounts = []

    def register(self, first_name, last_name, pin):
        account_name = f"{first_name} {last_name}"
        account_number = self.generate_account_number()
        new_account = Account(account_number, account_name, pin)
        self.accounts.append(new_account)

    def generate_account_number(self):
        return str(len(self.accounts) + 1)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        raise CustomError("Account not found")

    def deposit(self, amount, account_number):
        account = self.find_account(account_number)
        account.deposit(account_number, amount)

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        return account.check_balance(pin)

    def withdraw(self, amount, account_number, pin):
        account = self.find_account(account_number)
        account.withdraw(account.get_pin(), pin, amount)

    def transfer(self, amount, from_account_number, to_account_number, pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        from_account.transfer(from_account.get_pin(), to_account, amount)
