"""Housing Dictionary"""

Apartments = {
    "Apartment A" : 2300,
    "Apartment B" : 2100,
    "Apartment C" : 1800,
}


for apartment,monthly_rent in Apartments.items():
    annual_rent = monthly_rent * 12

    print(f"Monthly Rent of {apartment} is {monthly_rent} SAR and Annual Rent is {annual_rent} SAR")
