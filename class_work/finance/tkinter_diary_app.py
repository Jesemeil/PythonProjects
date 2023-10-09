import tkinter as tk
from tkinter import messagebox, simpledialog
from class_work.finance.diaries import Diaries, CustomError


class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diary App")

        self.diaries_manager = Diaries()
        self.current_diary = None

        tk.Label(root, text="Username:", width=16, height=5).grid(row=0, column=0)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1)

        tk.Label(root, text="Password:", width=16, height=5).grid(row=1, column=0)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1)

        register_button = tk.Button(root, text="Register", command=self.register, width=16, height=5)
        register_button.grid(row=2, column=0)

        login_button = tk.Button(root, text="Login", command=self.login, width=16, height=5)
        login_button.grid(row=2, column=1)

        view_entries_button = tk.Button(root, text="View Entries", command=self.view_entries, width=16, height=5)
        view_entries_button.grid(row=3, column=0)

        delete_entry_button = tk.Button(root, text="Delete Entry", command=self.delete_entry, width=16, height=5)
        delete_entry_button.grid(row=3, column=1)

        update_entry_button = tk.Button(root, text="Update Entry", command=self.update_entry, width=16, height=5)
        update_entry_button.grid(row=4, column=0)

        lock_diary_button = tk.Button(root, text="Lock Diary", command=self.lock_diary, width=16, height=5)
        lock_diary_button.grid(row=4, column=1)

        export_diary_button = tk.Button(root, text="Export Diary", command=self.export_diary, width=16, height=5)
        export_diary_button.grid(row=5, column=0)

        import_diary_button = tk.Button(root, text="Import Diary", command=self.import_diary, width=16, height=5)
        import_diary_button.grid(row=5, column=1)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            self.diaries_manager.add(username, password)
            tk.messagebox.showinfo("Success", "User registered successfully! You can now log in.")
        except CustomError as e:
            tk.messagebox.showerror("Error", str(e))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            diary = self.diaries_manager.find_by_username(username)
            if diary:
                diary.unlock_diary(password)
                self.current_diary = diary  # Set the current diary
                self.show_main_interface()
            else:
                tk.messagebox.showerror("Error", "Diary not found for this username.")
        except CustomError as e:
            tk.messagebox.showerror("Error", str(e))

    def show_main_interface(self):
        self.root.withdraw()

        main_window = tk.Tk()
        main_window.title("Diary App - Main Interface")

        tk.Label(main_window, text="Entry Title:").grid(row=0, column=0)
        entry_title_entry = tk.Entry(main_window)
        entry_title_entry.grid(row=0, column=1)

        tk.Label(main_window, text="Entry Body:").grid(row=1, column=0)
        entry_body_entry = tk.Entry(main_window)
        entry_body_entry.grid(row=1, column=1)

        create_entry_button = tk.Button(main_window, text="Create Entry",
                                        command=lambda: self.create_entry(entry_title_entry.get(),
                                                                          entry_body_entry.get()))
        create_entry_button.grid(row=2, columnspan=2)

        main_window.mainloop()

    def create_entry(self, title, body):
        try:
            self.current_diary.create_entry(title, body)
            tk.messagebox.showinfo("Success", "Entry created successfully!")
        except CustomError as e:
            tk.messagebox.showerror("Error", str(e))

    def view_entries(self):
        if self.current_diary:
            entries = self.current_diary.get_entries()
            if entries:
                entry_list_window = tk.Tk()
                entry_list_window.title("Diary Entries")

                entry_list = tk.Listbox(entry_list_window)
                entry_list.pack()

                for entry in entries:
                    entry_list.insert(tk.END, f"Title: {entry.get_title()}\nBody: {entry.get_body()}\n")

                entry_list_window.mainloop()
            else:
                tk.messagebox.showinfo("Info", "No entries found in this diary.")
        else:
            tk.messagebox.showerror("Error", "You need to log in first.")

    def delete_entry(self):
        if not self.current_diary:
            tk.messagebox.showerror("Error", "You need to log in first.")
            return

        try:
            entry_id = int(simpledialog.askstring("Delete Entry", "Enter the ID of the entry to delete:"))
            self.current_diary.delete_entry(entry_id)
            tk.messagebox.showinfo("Success", f"Entry with ID {entry_id} deleted successfully!")
        except CustomError as e:
            tk.messagebox.showerror("Error", str(e))
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid entry ID. Please enter a valid ID.")

    def update_entry(self):
        if not self.current_diary:
            tk.messagebox.showerror("Error", "You need to log in first.")
            return

        try:
            entry_id = int(simpledialog.askstring("Update Entry", "Enter the ID of the entry to update:"))
            entry_title = simpledialog.askstring("Update Entry", "Enter the new title:")
            entry_body = simpledialog.askstring("Update Entry", "Enter the new body:")

            if entry_title is not None and entry_body is not None:
                self.current_diary.update_entry(entry_id, entry_title, entry_body)
                tk.messagebox.showinfo("Success", f"Entry with ID {entry_id} updated successfully!")
            else:
                tk.messagebox.showerror("Error", "Both title and body are required to update an entry.")
        except CustomError as e:
            tk.messagebox.showerror("Error", str(e))
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid entry ID. Please enter a valid ID.")

    def lock_diary(self):
        if self.current_diary:
            self.current_diary.lock_diary()
            self.current_diary = None  # Reset the current diary
            tk.messagebox.showinfo("Info", "Diary locked. You have been logged out.")
            self.root.deiconify()
        else:
            tk.messagebox.showerror("Error", "You need to log in first.")

    def export_diary(self):
        if self.current_diary:
            try:
                filename = simpledialog.askstring("Export Diary", "Enter the file name to export to:")
                if filename:
                    with open(filename, 'w') as file:
                        entries = self.current_diary.get_entries()
                        for entry in entries:
                            file.write(f"Title: {entry.get_title()}\nBody: {entry.get_body()}\n\n")
                    tk.messagebox.showinfo("Success", f"Diary exported to {filename} successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            tk.messagebox.showerror("Error", "You need to log in first.")

    def import_diary(self):
        if self.current_diary:
            try:
                filename = simpledialog.askstring("Import Diary", "Enter the file name to import from:")
                if filename:
                    with open(filename, 'r') as file:
                        lines = file.readlines()
                        title = None
                        body = ""
                        for line in lines:
                            line = line.strip()
                            if line.startswith("Title: "):
                                title = line[len("Title: "):]
                            elif line.startswith("Body: "):
                                body = line[len("Body: "):]
                            elif not line:
                                if title and body:
                                    self.current_diary.create_entry(title, body)
                                    title = None
                                    body = ""
                        if title and body:
                            self.current_diary.create_entry(title, body)
                    tk.messagebox.showinfo("Success", f"Diary imported from {filename} successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            tk.messagebox.showerror("Error", "You need to log in first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
