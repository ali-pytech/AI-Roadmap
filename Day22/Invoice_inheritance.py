"""VAT Invoice Inheritance"""

class Transection:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def summery(self):
        return f"Transection: {self.item} | Price: {self.price} SAR"
    
class Invoice(Transection):
    def __init__(self, item, price, quantity, vat_rate):
        super().__init__(item, price)
        self.quantity = quantity
        self.vat_rate = vat_rate

    def summery(self):
        total = self.price * self.quantity *(1 + self.vat_rate)
        return f"Invoice: Item: {self.item} | Quantity: {self.quantity} | Total Price With VAT: {total}"
    
Laptop = Invoice("Laptop", 2500, 3, 0.15)
print(Laptop.summery())
