import unittest

from class_work.finance.account import CustomError
from class_work.finance.diaries import Diaries


class TestDiaries(unittest.TestCase):

    def setUp(self):
        self.diaries = Diaries()

    def test_add_diary(self):
        self.diaries.add("testuser1", "password1")
        self.assertEqual(len(self.diaries.get_diaries()), 1)

    def test_find_by_username_existing(self):
        self.diaries.add("testuser1", "password1")
        found_diary = self.diaries.find_by_username("testuser1")
        self.assertIsNotNone(found_diary)
        self.assertEqual(found_diary.get_username(), "testuser1")

    def test_find_by_username_non_existing(self):
        found_diary = self.diaries.find_by_username("non_existing_user")
        self.assertIsNone(found_diary)

    def test_delete_diary_correct_password(self):
        self.diaries.add("testuser1", "password1")
        self.diaries.delete("testuser1", "password1")
        self.assertEqual(len(self.diaries.get_diaries()), 0)

    def test_delete_diary_incorrect_password(self):
        self.diaries.add("testuser1", "password1")
        with self.assertRaises(CustomError):
            self.diaries.delete("testuser1", "wrongpassword")

    def test_delete_diary_non_existing_user(self):
        with self.assertRaises(CustomError):
            self.diaries.delete("non_existing_user", "password1")


if __name__ == '__main__':
    unittest.main()
