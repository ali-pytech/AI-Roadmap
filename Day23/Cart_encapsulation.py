"""Shopping Cart Encapsulation"""

class CartItem:
    def __init__(self, item, price, quantity):
        self.item = item
        self.__price = price
        self.quantity = quantity

        
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid Price!!")

    def subtotal(self):
        return self.__price * self.quantity
    

shoes = CartItem ("Shoes", 230, 3)
print("Initial Price:", shoes.subtotal())
shoes.set_price(250)
print("Updated Price:", shoes.subtotal())
