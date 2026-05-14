""""Smart Service Portal"""

from abc import  ABC, abstractmethod

#abstract base class
class Service(ABC):
    @abstractmethod
    def process(self):
        pass

#Encapsulation and Inheritance

class Iqama(Service):
    def __init__(self, holder, year, fee):
        self.holder = holder
        self.year = year
        self.__fee = fee #private attribute

    def get_fee(self):
        return self.__fee
    
    def set_fee(self, new_fee):
        if new_fee > 0:
            self.__fee = new_fee

        else:
            print("Invalid Fee!!")

    def process(self):    #polymorphism
        return f"Iqama Renewed For {self.holder} | Fee: {self.__fee} SAR"
    
class Invoice(Service):
    def __init__(self, item, price, quantity, vat_rate):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.vat_rate = vat_rate

    def process(self):
        total = self.price * self.quantity * (1 + self.vat_rate)
        return f" Invoice For: {self.item} | Quantity: {self.quantity} | Total With VAT: {total:.2f} SAR"
    

class Housing(Service):
    def __init__(self, apartment, monthly_rent):
        self.apartment = apartment
        self.__monthly_rent = monthly_rent

    def get_rent(self):
        return self.__monthly_rent
    
    def set_rent(self, new_rent):
        if new_rent >= 1000:
            self.__monthly_rent = new_rent

        else:
            print("Invalid Rent!!")

    def process(self):
        return f"Housing Record: {self.apartment} | Annual rent: {self.__monthly_rent * 12}"
    #polymorphism

Services = [
        Iqama("Ali",  2026, 800),
        Invoice("Laptop", 3000, 2, 0.15),
        Housing("Apartment A", 2500)
]

for s in Services:
    print(s.process())
