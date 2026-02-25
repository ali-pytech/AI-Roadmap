"""VAT Calculator Functions"""

def calculate_VAT(price , quantity , vat_rate=0.15):
    subtotal = price * quantity
    return subtotal * (1 + vat_rate)

print(f"Laptop : {calculate_VAT(1200,2)} SAR")
print(f"IPAD : {calculate_VAT(900,3)} SAR")
