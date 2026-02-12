"""VAT Invoice"""
items = {
    "Laptop": {"price": 3000, "quantity": 2},
    "Phone": {"price": 2000, "quantity": 3},
    "Tablet": {"price": 1500, "quantity": 1}
}

# Delete Tablet record
del items["Tablet"]

# Adding New item
items["Charger"] = {"price":200, "quantity":1}

print(items)
