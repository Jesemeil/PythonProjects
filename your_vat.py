def your_vat():
    while True:
        try:
            price = float(input("Enter the price of the item: "))
            if price < 0:
                print("Price cannot be negative. Please enter a non-negative price.")
                continue

            while True:
                vat_percentage = float(input("Enter the VAT percentage: "))
                if vat_percentage < 0:
                    print("VAT percentage cannot be negative. Please enter a non-negative VAT percentage.")
                else:
                    break

            vat_inclusive_price = price + (vat_percentage / 100 * price)
            return vat_inclusive_price
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


vat_inclusive_price = your_vat()
print("VAT inclusive price:", vat_inclusive_price)
