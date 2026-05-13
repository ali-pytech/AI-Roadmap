"""VAT invoice Abstraction"""

from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def summery(self):
        pass

class Invoice(Transaction):
    def __init__(self, item, price, quantity, vat_rate):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.vat_rate = vat_rate

    def summery(self):
        total = self.price * self.quantity * (1 + self.vat_rate)
        return f" Invoice:  Item: {self.item} | Quantity: {self.quantity} | Total Price with VAT: {total:.2f}"
    
laptop = Invoice("Laptop", 3000, 2, 0.15)
print(laptop.summery())
