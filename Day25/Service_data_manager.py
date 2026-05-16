
"""Service DATA Manager"""

import json
from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def process(self):
        pass

class Iqama(Service):
    def __init__(self, holder, year, fee):
        self.holder = holder
        self.year = year
        self.__fee = fee
    def get_fee(self):
        return self.__fee
    
    def set_fee(self, new_fee):
        if new_fee > 0:
            self.__fee = new_fee

    def process(self):
        return f"Iqma Renewed For: {self.holder} | Year: {self.year} | Fee: {self.__fee} SAR "
    

class Invoice(Service):
    def __init__(self, item, price, quantity, vat_rate):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.vat_rate = vat_rate

    def process(self):
        total = self.price * self.quantity * (1 + self.vat_rate)
        return f"Invoice: Item: {self.item} Price: {self.price} Quantity: {self.quantity} Total price with VAT: {total:.2f} SAR"
    
class Housing(Service):
    def __init__(self, apartment, monthly_rent):
        self.apartment = apartment
        self.__monthly_rent = monthly_rent

    def get_rent(self):
        return self.__monthly_rent
    
    def set_rent(self, new_rent):
        if new_rent > 1000:
            self.__monthly_rent = new_rent

    def process(self):
        return f"Housing record: {self.apartment}  Annual Rent: {self.__monthly_rent * 12} SAR"
    
Services = [
    Iqama("Ahmed", 2026, 700),
    Invoice("Laptop", 3200, 2, 0.15),
    Housing("Apartment A", 2700)

]

data =[s.process() for s in Services]

with open("Services.json", "w") as f:
    json.dump(data, f, indent=4)

#load Data from json File

with open("Services.json", "r") as f:
    loaded_data = json.load(f)

print("Data Loaded From File:")
for record in loaded_data:
    print(record)




