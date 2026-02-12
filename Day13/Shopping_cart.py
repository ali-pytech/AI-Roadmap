"""Shopping Cart System"""

cart = {
    "T-shirt": {"price":70, "Quantity":3, "Discount":0.15},  #15% Discount
    "Shoes": {"price":120, "Quantity":2, "Discount":0.20},   #20% Discount
    "Watch": {"price":230, "Quantity":1, "Discount":0.30}    #30% Discount
}

for product , details in cart.items():
    subtotal = details['price'] * details['Quantity']
    discount_amount = subtotal * details['Discount']
    final_total = subtotal - discount_amount
    print(f"Item: {product} | Quantity: {details['Quantity']} | Price: {details['price']} SAR |  Discounted Price: {final_total} SAR") 
