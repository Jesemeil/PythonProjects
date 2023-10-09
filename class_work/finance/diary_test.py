import unittest

from class_work.finance.account import CustomError
from diary import Diary


class TestDiary(unittest.TestCase):

    def setUp(self):
        self.diary = Diary("testuser", "password")

    def test_unlock_diary_correct_password(self):
        self.diary.unlock_diary("password")
        self.assertFalse(self.diary.is_locked_status())

    def test_unlock_diary_incorrect_password(self):
        with self.assertRaises(CustomError):
            self.diary.unlock_diary("wrongpassword")

    def test_lock_diary(self):
        self.diary.unlock_diary("password")
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked_status())

    def test_create_entry_unlocked_diary(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("EntryTitle", "EntryBody")
        self.assertEqual(len(self.diary.get_entries()), 1)

    def test_create_entry_locked_diary(self):
        with self.assertRaises(CustomError):
            self.diary.create_entry("EntryTitle", "EntryBody")

    def test_delete_entry_unlocked_diary(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("EntryTitle", "EntryBody")
        self.diary.delete_entry(1)
        self.assertEqual(len(self.diary.get_entries()), 0)

    def test_delete_entry_locked_diary(self):
        with self.assertRaises(CustomError):
            self.diary.delete_entry(1)

    def test_find_entry_by_id_existing(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("EntryTitle", "EntryBody")
        found_entry = self.diary.find_entry_by_id(1)
        self.assertIsNotNone(found_entry)
        self.assertEqual(found_entry.get_title(), "EntryTitle")
        self.assertEqual(found_entry.get_body(), "EntryBody")

    def test_find_entry_by_id_non_existing(self):
        self.diary.unlock_diary("password")
        with self.assertRaises(CustomError):
            self.diary.find_entry_by_id(1)  # Attempt to find a non-existing entry

    def test_update_entry_existing(self):
        self.diary.unlock_diary("password")
        self.diary.create_entry("EntryTitle", "EntryBody")
        self.diary.update_entry(1, "NewTitle", "NewBody")
        updated_entry = self.diary.find_entry_by_id(1)
        self.assertIsNotNone(updated_entry)
        self.assertEqual(updated_entry.get_title(), "NewTitle")
        self.assertEqual(updated_entry.get_body(), "NewBody")

    def test_update_entry_non_existing(self):
        with self.assertRaises(CustomError):
            self.diary.update_entry(1, "NewTitle", "NewBody")


if __name__ == '__main__':
    unittest.main()
