"""Housing Intersection"""
Riyadh_apartments = {"Apartment A", "Apartment D", "Apartment E"}
Affordable_apartments = {"Apartment C", "Apartment E", "Apartment A"}

common_apartments = Riyadh_apartments & Affordable_apartments
print(f"Affordable Riyadh Apaprtments: {common_apartments}")
