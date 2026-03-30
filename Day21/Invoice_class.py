"""VAT Invoice Class"""

class Invoice:
    def __init__(self, item, price, quantity, vat_rate):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.vat_rate = vat_rate

    def total(self):
        return self.price * self.quantity * (1 + self.vat_rate)

laptop = Invoice("Laptop", 3000, 2, 0.15)
phone = Invoice("Phone", 2000, 3, 0.15)

print("Invoices:")
print(laptop.item, "-", laptop.total())
print(phone.item, "-", phone.total())
