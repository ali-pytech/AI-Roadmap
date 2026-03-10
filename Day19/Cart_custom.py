
class CartError(Exception):
    pass 

def add_item(name, price, quantity):
    if quantity <= 0:
        raise CartError("Quantity Must be Greater than Zero")
    return {"Item": name, "Price":price, "Quantity":quantity, "subtotal":price*quantity}

try:
    shoes =  add_item ("Shoes",200,2)
    shirt = add_item ("T-shirt",50,0)  #invalid
    cart = [shoes, shirt]

    print("Shopping Cart:",cart)

except CartError as c:
    print("Error", c)
