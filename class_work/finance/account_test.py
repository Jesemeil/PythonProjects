import unittest
from account import Account, CustomError


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account("1", "Paul Obi", "1234")

    def test_depositMoney_balanceIncreases(self):
        self.assertEqual(0, self.account.check_balance("1234"))
        self.account.deposit("1", 6000)
        self.assertEqual(6000, self.account.check_balance("1234"))
        self.account.deposit("1", 5000)
        self.assertEqual(11000, self.account.check_balance("1234"))

    def test_depositNegativeAmount_throwsException(self):
        self.assertEqual(0, self.account.check_balance("1234"))
        with self.assertRaises(CustomError):
            self.account.deposit("1", -100)

    def test_withdrawMoneyWithCorrectPin_balanceDecreases(self):
        self.account.deposit("1", 20000)
        self.assertEqual(20000, self.account.check_balance("1234"))
        self.account.withdraw("1234", "1234", 12000)
        self.assertEqual(8000, self.account.check_balance("1234"))

    def test_withdrawMoney_withWrongPinException(self):
        self.account.deposit("1", 4000)
        with self.assertRaises(CustomError):
            self.account.withdraw("1123", "1234", 2000)

    def test_withdrawMoney_greaterThanBalanceThrowsException(self):
        self.account.deposit("1", 3000)
        with self.assertRaises(CustomError):
            self.account.withdraw("1234", "1234", 4000)

    def test_check_balance(self):
        self.account.deposit("1", 7000)
        self.assertEqual(7000, self.account.check_balance("1234"))

    def test_validatePin_withCorrectPin(self):
        self.assertTrue(self.account._validate_pin("1234"))

    def test_validatePin_withWrongPin(self):
        self.assertTrue(self.account._validate_pin("1234"))
        with self.assertRaises(CustomError):
            self.account._validate_pin("2143")

    def test_updatePin_Successful(self):
        self.assertTrue(self.account._validate_pin("1234"))
        self.account.update_pin("1234", "4715")
        self.assertTrue(self.account._validate_pin("4715"))

    def test_updatePin_invalidPinException(self):
        self.assertTrue(self.account._validate_pin("1234"))
        with self.assertRaises(CustomError):
            self.account.update_pin("4565", "1245")


if __name__ == '__main__':
    unittest.main()
