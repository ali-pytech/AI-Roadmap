"""Shopping Cart Class"""

class CartItem:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
    
    def subtotal(self):
        return self.price * self.quantity
    

shoes = CartItem("Shoes", 150, 3)
shirt = CartItem("T-shirt", 100,2)

print("Shopping Cart")
print(shoes.item, "--", shoes.subtotal())
print(shirt.item, "--", shirt.subtotal())
