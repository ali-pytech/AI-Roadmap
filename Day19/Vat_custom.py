
class InvalidVATError(Exception):
    pass

def create_invoice(item, price, quantity, vat_rate):
    if not (0 <= vat_rate <= 1):
        raise InvalidVATError("VAT Rate must be Between 0 to 1")
    subtotal = price * quantity
    total  =  subtotal * (1 + vat_rate)
    return {"item": item, "Price": price, "Quantity": quantity, "VAT_rate":vat_rate, "Total": total}

try:
    laptop_invoice = create_invoice("Laptop", 3000, 1, 0.15)
    phone_invoice = create_invoice("Phone",4500,2,1.15)  # invalid
    invoices = [laptop_invoice, phone_invoice]
    print("Invoices:",invoices)


except InvalidVATError as i:
    print("Error:", i)
