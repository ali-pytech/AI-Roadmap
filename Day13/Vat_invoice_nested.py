"""VAT Invoice with Item Details"""

Items = {
    "Laptop": {"price": 4000, "quantity": 2},
    "Mobile": {"price": 5500, "quantity": 1},
    "IPad": {"price": 6200, "quantity": 3}
}

vat_rate=0.15

for item , details in Items.items():
    total = (details['price'] * details['quantity']) * (1 + vat_rate)

    print(f"{item}: Quantity: {details['quantity']}  Price: {details['price']} SAR Total Price with VAT: {total:.2f} SAR")
