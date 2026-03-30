"""Housing Class"""

class Housing:
    def __init__(self, apartment, monthly_rent):
        self.apartment = apartment
        self.monthly_rent = monthly_rent

    def annual_rent(self):
        return self.monthly_rent * 12
    
apt_A = Housing("Apartment A", 2500)
apt_B = Housing("Apartment B", 2100)

print("Housing Record:")
print(apt_A.apartment, "--", apt_A.annual_rent())
print(apt_B.apartment, "--", apt_B.annual_rent())
