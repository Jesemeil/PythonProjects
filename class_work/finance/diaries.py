from class_work.finance.account import CustomError
from class_work.finance.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        new_diary = Diary(username, password)
        self.diaries.append(new_diary)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary
        return None

    def delete(self, username, password):
        diary_to_delete = self.find_by_username(username)
        if diary_to_delete:
            if diary_to_delete.get_password() == password:
                self.diaries.remove(diary_to_delete)
            else:
                raise CustomError("Incorrect password")
        else:
            raise CustomError(f"Diary for username {username} not found")

    def get_diaries(self):
        return self.diaries
