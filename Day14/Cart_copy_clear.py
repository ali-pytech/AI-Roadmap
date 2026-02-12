"""Shopping Cart copy and Clear"""

cart = {
    "T-shirt": {"price":70, "Quantity":3, "Discount":0.15},  
    "Shoes": {"price":120, "Quantity":2, "Discount":0.20},   
    "Watch": {"price":230, "Quantity":1, "Discount":0.30}   
}

#copy Cart
cart_copy = cart.copy()
print("copied cart",cart_copy)

#clear original cart
cart.clear()
print("Original Cart after clear", cart)
