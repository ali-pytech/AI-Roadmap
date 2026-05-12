"""Shopping Cart Polymorphism"""

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def description(self):
        return f" Item: {self.name} Price: {self.price}"
    
class CartItem(Item):
    def __init__(self, name, price, quantity):
      super().__init__(name, price)
      self.quantity = quantity

    def description(self):
        return f" Item: {self.name} | Quantity: {self.quantity} | Total Price: {self.quantity * self.price}"
    
shoes = CartItem("Shoes", 250, 2)
shirt = CartItem("T-shirt", 100, 3)

print(shoes.description())
print(shirt.description())
