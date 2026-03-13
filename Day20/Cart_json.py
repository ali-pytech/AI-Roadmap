
"""Shopping Cart Json"""

import json

cart = [
    {"Item":"Shoes" , "price":100 ,"Quantity": 3 , "Subtotal":300},
    {"Item":"Bag" , "price":200 ,"Quantity": 2 , "Subtotal":400}

]


with open("cart.json", "w") as file:
    json.dump(cart, file,  indent=4)

with open("cart.json", "r") as file:
    data = json.load(file)
    print("Cart File Content:\n",data)
