"""VAT Division Error"""

def vat_per_item(total, quantity):
    try:
        return total / quantity 
    
    except ZeroDivisionError:
        print("Cannot be Divided by Zero.")

print(f"Result:{vat_per_item(3200,3)}")
print(f"Result: {vat_per_item(2700,2)}")
