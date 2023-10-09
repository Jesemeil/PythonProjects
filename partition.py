from typing import re

date = "victor"
dates = date.rpartition("o")
dates_1 = date.partition("c")
dates_2 = date.split("o")
dates_3 = date.upper()
dates_4 = date.splitlines()
print(dates)
print(dates_1)
print(dates_2)
print(dates_3)
print(dates_4)

print("yes" if re.fullmatch(r"[A-Z]{2}[a-z]", "400001") else "NO")

print(re.sub(r'\t', ',', '))