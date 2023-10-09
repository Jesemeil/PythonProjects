from datetime import datetime


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity


def main():
    products = []
    customer_name = input("What is the customer's name?\n")

    while True:
        product_name = input("What did the user buy?\n")

        quantity = int(input("How many pieces?\n"))

        price = float(input("How much per unit?\n"))

        products.append(Product(product_name, price, quantity))

        more_items = input("Add more items? (Yes/No)\n").strip().lower()
        if more_items == "no":
            break

    cashier_name = input("What is your name? (Cashier's name)\n")
    discount_percentage = float(input("How much discount will the customer get? (Enter a percentage)\n"))

    total = sum(product.get_total_price() for product in products)
    discount_amount = total * (discount_percentage / 100)
    vat = total * 0.175
    bill_total = total - discount_amount + vat

    print("\nSEMICOLON STORES")
    print("MAIN BRANCH")
    print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    print("TEL: 83293828343")
    print(f"Date: {datetime.now().strftime('%d-%b-%y %I:%M:%S%p')}")
    print(f"Cashier: {cashier_name}")
    print(f"Customer Name: {customer_name}")
    print(
        "=================================================================================================================")
    print("          ITEM                  QTY              PRICE         TOTAL(NGN)")
    print(
        "-----------------------------------------------------------------------------------------------------------------")
    for product in products:
        print(f"{product.name:15}{product.quantity:20d}{product.price:20.2f}{product.get_total_price():20.2f}")
    print(
        "-----------------------------------------------------------------------------------------------------------------")
    print(f"{'Sub Total:':55}{total:.2f}")
    print(f"{'Discount:':55}{discount_amount:.2f}")
    print(f"{'VAT@ 17.5%:':55}{vat:.2f}")
    print(
        "=================================================================================================================")
    print(f"{'BILL TOTAL:':55}{bill_total:.2f}")
    print(
        "=================================================================================================================")
    print(
        "=================================================================================================================")
    print(f"{'THIS IS NOT A RECEIPT KINDLY PAY':55}{bill_total:.2f}")
    print(
        "=================================================================================================================")

    amount_paid = float(input("How much did the customer give to you?\n"))
    balance = amount_paid - bill_total

    print("\nSEMICOLON STORES")
    print("MAIN BRANCH")
    print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")
    print("TEL: 83293828343")
    print(f"Date: {datetime.now().strftime('%d-%b-%y %I:%M:%S%p')}")
    print(f"Cashier: {cashier_name}")
    print(f"Customer Name: {customer_name}")
    print(
        "=================================================================================================================")
    print("          ITEM                  QTY              PRICE         TOTAL(NGN)")
    print(
        "-----------------------------------------------------------------------------------------------------------------")
    for product in products:
        print(f"{product.name:15}{product.quantity:20d}{product.price:20.2f}{product.get_total_price():20.2f}")
    print(
        "-----------------------------------------------------------------------------------------------------------------")
    print(f"{'Sub Total:':55}{total:.2f}")
    print(f"{'Discount:':55}{discount_amount:.2f}")
    print(f"{'VAT@ 17.5%:':55}{vat:.2f}")
    print(
        "=================================================================================================================")
    print(f"{'BILL TOTAL:':55}{bill_total:.2f}")
    print(f"{'AMOUNT PAID:':55}{amount_paid:.2f}")
    print(f"{'BALANCE:':55}{balance:.2f}")
    print(
        "=================================================================================================================")
    print("\n\nTHANK YOU FOR YOUR PATRONAGE")
    print(
        "=================================================================================================================")


if __name__ == "__main__":
    main()
