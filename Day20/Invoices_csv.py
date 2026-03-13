"""VAT Invoices CSV"""

import csv

invoices = [
    {"item": "Laptop", "price": 3000, "quantity": 2, "vat_rate": 0.15},
    {"item": "Phone", "price": 2000, "quantity": 3, "vat_rate": 0.15}
]

# Write to CSV

with open("invoices.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames = ['item', 'price', 'quantity', 'vat_rate'])
    writer.writeheader()
    writer.writerows(invoices)

with open("invoices.csv", "r") as file:
    print("Invoices File Content:\n",file.read())
