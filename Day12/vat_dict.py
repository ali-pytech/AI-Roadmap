"""VAT Dictionary"""

Items = {
    "Laptop": 2000,
    "Mobile":5500,
    "IPad":6200
}

vat_rate=0.15

for item, price in Items.items():
    vat = price * vat_rate
    total = vat + price

    print(f"On {item} VAT is {vat} and total price will be {total}")
