""Apartment Record"""
Apartments = {
    "Apartment A" : {"monthly_rent": 2300, "Location": "Riyadh", "Size": "2 Bedroom"},
    "Apartment B" : {"monthly_rent": 2100, "Location": "Jeddah", "Size": "3 Bedroom"},
    "Apartment C" : {"monthly_rent": 1800, "Location": "Dammam", "Size": "Studio"}
}
for apartment , details in Apartments.items():
    annual_rent = details['monthly_rent'] * 12
    print(f"{apartment} Monthly Rent: {details['monthly_rent']} SAR Location: {details['Location']} Annual Rent: {annual_rent} SAR")
 
