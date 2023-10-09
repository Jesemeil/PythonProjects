import re


def email_validator(emails):
    valid_emails = []
    for email in emails:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(pattern, email):
            valid_emails.append(email)

    return valid_emails


valid_emails1 = email_validator(["john@example.com", "@invalid.com", "jane@gmail.", "test@co", "info@africa"])
print(valid_emails1)
