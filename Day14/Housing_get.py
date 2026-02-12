"""Housing Easy Access"""
housing = {
    "Apartment A": {"monthly_rent": 2500, "location": "Riyadh"},
    "Apartment B": {"monthly_rent": 3000, "location": "Jeddah"}
}

# Safe access using .get()
print(housing.get("Apartment A", "Not Found"))
print(housing.get("Apartment C", "Not Found"))
