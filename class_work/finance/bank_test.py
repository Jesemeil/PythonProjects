import unittest
from bank import Bank
from class_work.finance.account import CustomError


class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_registerAnd_findAccount(self):
        self.bank.register("Paul", "Obi", "1234")

        self.bank.register("Daniel", "Obasa", "2545")

    def test_findAccount_notFound(self):
        with self.assertRaises(CustomError):
            self.bank.find_account("1")

    def test_depositMoney_balanceIncreases(self):
        self.bank.register("Paul", "Obi",
                           "1234")

        self.bank.deposit(2000, "1")
        self.assertEqual(2000, self.bank.check_balance("1", "1234"))

        self.bank.deposit(3000, "1")
        self.assertEqual(5000, self.bank.check_balance("1", "1234"))

    def test_withdrawMoney_balanceDecreases(self):
        self.bank.register("Paul", "Obi", "1234")
        self.bank.deposit(4000, "1")
        self.bank.withdraw(1000, "1", "1234")
        self.assertEqual(3000, self.bank.check_balance("1", "1234"))

    def test_transferFrom_accountNumber_to_another_AccountNumber(self):
        self.bank.register("Paul", "Obi", "1234")
        self.bank.register("Kate", "Hank", "4235")
        self.bank.deposit(8000, "1")
        self.bank.transfer(2500, "1", "2", "1234")
        self.assertEqual(5500, self.bank.check_balance("1", "1234"))
        self.assertEqual(2500, self.bank.check_balance("2", "4235"))

    def test_check_balance(self):
        self.bank.register("Paul", "Obi", "1234")
        self.assertEqual(0, self.bank.check_balance("1", "1234"))
        self.bank.deposit(8000, "1")
        self.assertEqual(8000, self.bank.check_balance("1", "1234"))


if __name__ == '__main__':
    unittest.main()
