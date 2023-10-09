import unittest
from entry import Entry


class TestEntry(unittest.TestCase):

    def test_entry_constructor(self):
        entry = Entry(1, "Title", "Body")
        self.assertEqual(entry.get_id(), 1)
        self.assertEqual(entry.get_title(), "Title")
        self.assertEqual(entry.get_body(), "Body")


if __name__ == '__main__':
    unittest.main()
