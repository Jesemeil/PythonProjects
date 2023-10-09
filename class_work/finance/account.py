class CustomError(Exception):
    def __int__(self, message):
        self.message = message


class Account:
    def __init__(self, account_number, account_name, pin):
        self.account_number = account_number
        self.account_name = account_name
        self.pin = pin
        self.balance = 0

    def check_balance(self, entered_pin):
        self._validate_pin(entered_pin)
        return self.balance

    def _validate_pin(self, entered_pin):
        if self.pin != entered_pin:
            raise CustomError("Invalid pin")
        return True

    def deposit(self, account_number, amount):
        self.account_number = account_number
        if amount <= 0:
            raise CustomError("Amount must be greater than zero")
        self.balance += amount

    def withdraw(self, entered_pin, withdrawal_pin, amount):
        self.pin = withdrawal_pin
        self._validate_pin(entered_pin)
        if amount > self.balance:
            raise CustomError("Insufficient balance")
        else:
            self.balance -= amount

    def update_pin(self, old_pin, new_pin):
        self._validate_pin(old_pin)
        self.pin = new_pin

    def transfer(self, pin, to_account, amount):
        self._validate_pin(pin)
        if self.balance < amount:
            raise CustomError("Insufficient balance")
        self.balance -= amount
        to_account._receive_transfer(amount)

    def _receive_transfer(self, amount):
        self.balance += amount

    def get_account_number(self):
        return self.account_number

    def get_account_name(self):
        return self.account_name

    def get_pin(self):
        return self.pin
