"""VAT Invoice Totals"""

Items = {
    "Laptop": {"price": 4000, "quantity": 2},
    "Mobile": {"price": 5500, "quantity": 1},
    "IPad": {"price": 6200, "quantity": 3}
}
 
vat_rate = 0.15
grand_total=0

for item , details in Items.items():
    total = (details['price'] * details['quantity']) * (1 + vat_rate)
    grand_total += total 
    print(f"{item}: {total:.2f} SAR")

print(f"Grand Total With VAT: {grand_total} SAR")
