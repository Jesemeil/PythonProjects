import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

name = simpledialog.askstring("Input", "Enter your name:")
print("Hello,", name, "!")
