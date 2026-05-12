"""Housing Inheritance"""

class Property:
    def __init__(self, name, monthly_rent):
        self.name = name
        self.monthly_rent = monthly_rent

    def details(self):
        return f"Property: {self.name} | Monthly Rent: {self.monthly_rent}"
    
class Housing(Property):
    def annual_rent(self):
        return self.monthly_rent * 12 
    
Aprt_A = Housing("Apartment A", 3000)
print(Aprt_A.details())
print("Annual Rent:", Aprt_A.annual_rent())
