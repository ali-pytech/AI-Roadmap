
class RentError(Exception):
    pass

def create_housing_record(name, monthly_rent):
    if monthly_rent < 1000:
        raise RentError ("Monthly Rent is Too Low for Riyadh Housing")
    
    return {"Apartment": name  , "Monthly Rent": monthly_rent , "Annual Rent": monthly_rent*12}

try:
    apt_a = create_housing_record("Apartment A", 2500)
    apt_b = create_housing_record("Apartment B", 500)
    housing_record = [apt_a , apt_b]
    print("Housing Record: ", housing_record)

except RentError as r:
    print("Error:", r)
