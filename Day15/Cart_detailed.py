"""Shopping Cart Detailed Output"""

cart = { 
    "Shoes": {"price": 200, "quantity": 2},
    "Shirt": {"price": 150, "quantity": 3}, 
    "Watch": {"price": 500, "quantity": 1} 
}

print("Shopping Cart Details")
for product , details in cart.items():
    subtotal = details['price'] * details['quantity']
    print(f"{product} : {details['quantity']} x {details['price']} SAR | {subtotal} SAR")
