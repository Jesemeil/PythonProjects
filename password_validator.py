import re


def password_validator():
    while True:
        password = input("Please enter a password: ")

        errors = []

        if len(password) < 8:
            errors.append("Password should be at least 8 characters long.")

        if not re.search(r'\d', password):
            errors.append("Password should contain at least one number.")

        if not re.search(r'[A-Z]', password):
            errors.append("Password should contain at least one uppercase letter.")

        if not re.search(r'[a-z]', password):
            errors.append("Password should contain at least one lowercase letter.")

        if not errors:
            return password
        else:
            print("Invalid password. The following errors were found:")
            for error in errors:
                print(error)


valid_password = password_validator()
print(f"Valid password: {valid_password}")

