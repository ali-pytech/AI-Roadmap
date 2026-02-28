"""Shopping Cart CleanUP"""

try:
    cart = {"shoes":150, "T-shirt":70}
    total = cart["shoes"] + cart["Watch"]    #as Watch Does not exist
    print(f"Total : {total}")

except KeyError:
    print("Item Not Found in Cart!!!")

finally:
    print("Cart Check Complete.")
