"""Housing Encapsulation"""

class Housing:
    def __init__(self, apartment, monthly_rent):
        self.apartment = apartment
        self.__monthly_rent = monthly_rent   #private attribute

    def get_rent(self):
        return self.__monthly_rent
    
    def set_rent(self, new_rent):
        if new_rent >= 1000:
            self.__monthly_rent = new_rent

        else:
            print("Rent Too Low!!")

apart_a = Housing("Apartment A", 1900)
print("Initial Rent:", apart_a.get_rent())
apart_a.set_rent(3000)
print("Updated Rent:", apart_a.get_rent())
