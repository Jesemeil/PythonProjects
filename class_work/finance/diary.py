from class_work.finance.account import CustomError
from entry import Entry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._is_locked = True
        self.entries = []

    def unlock_diary(self, password):
        if password == self.password:
            self._is_locked = False
        else:
            raise CustomError("Incorrect password")

    def lock_diary(self):
        self._is_locked = True

    def is_locked_status(self):
        return self._is_locked

    def create_entry(self, title, body):
        if not self._is_locked:
            new_entry = Entry(len(self.entries) + 1, title, body)
            self.entries.append(new_entry)
        else:
            raise CustomError("Diary is locked, cannot create entry")

    def delete_entry(self, id):
        if not self._is_locked:
            found = False
            for entry in self.entries:
                if entry.id == id:
                    self.entries.remove(entry)
                    found = True
                    break
            if not found:
                raise CustomError(f"Entry with ID {id} not found")
        else:
            raise CustomError("Diary is locked, cannot delete entry")

    def find_entry_by_id(self, id):
        if not self._is_locked:
            for entry in self.entries:
                if entry.id == id:
                    return entry
            raise CustomError(f"Entry with ID {id} not found")
        return None

    def update_entry(self, id, new_title, new_body):
        if not self._is_locked:
            entry_to_update = self.find_entry_by_id(id)
            if entry_to_update:
                entry_to_update.title = new_title
                entry_to_update.body = new_body
            else:
                raise CustomError(f"Entry with ID {id} not found")
        else:
            raise CustomError("Diary is locked, cannot update entry")

    def get_entries(self):
        return self.entries

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
