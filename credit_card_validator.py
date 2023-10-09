def luhn_algorithm(card_number):
    digits = [int(digit) for digit in str(card_number)][::-1]

    doubled_digits = [digit * 2 if i % 2 else digit for i, digit in enumerate(digits)]

    subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]

    total_sum = sum(subtracted_digits)

    return total_sum % 10 == 0


def validate_credit_card(card_number):
    card_length = len(str(card_number))
    card_type = ""

    if card_length == 16 and str(card_number).startswith("4"):
        card_type = "Visa"
    elif card_length == 16 and str(card_number).startswith("5"):
        card_type = "MasterCard"
    elif card_length == 15 and str(card_number).startswith("37"):
        card_type = "American Express"
    elif card_length == 16 and str(card_number).startswith("6"):
        card_type = "Discover"
    else:
        card_type = "Invalid Card"

    is_valid = luhn_algorithm(card_number)

    output = f"""*************************************************
**Credit Card Type: {card_type}
**Credit Card Number: {card_number}
**Credit Card Digit Length: {card_length}
**Credit Card Validity: {'Valid' if is_valid else 'Invalid'}
**************************************************"""

    return output


if __name__ == "__main__":
    while True:
        print("Hello, kindly enter the card details to verify:")
        card_number = input().strip()
        try:
            card_number = int(card_number)
            result = validate_credit_card(card_number)
            print(result)
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric card number.")
