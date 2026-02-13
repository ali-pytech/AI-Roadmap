"""Affordable Apartment Finder"""

housing = {
    "Apartment A": {"monthly_rent": 2500, "location": "Riyadh"},
    "Apartment B": {"monthly_rent": 3000, "location": "Jeddah"},
    "Apartment C": {"monthly_rent": 1800, "location": "Dammam"}
}

print("Affordable Apartments (Rent < 2500 SAR):")
for apartment, details in housing.items():
    if details["monthly_rent"] < 2500:
        print(f"{apartment} - Location: {details['location']}, Rent: {details['monthly_rent']} SAR")
