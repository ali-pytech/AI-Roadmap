
"""Service Record  Manager"""

import csv
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

    def process(self):

        return [self.holder, self.year, self.__fee]
    
class Invoice(Service):
    def __init__(self, item, price, quantity, vat_rate):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.vat_rate = vat_rate

    def process(self):
        total = self.price * self.quantity * (1 +self.vat_rate)
        return [self.item, self.price, self.quantity, self.vat_rate, total]
    

class Housing(Service):
    def __init__(self, apartment,  monthly_rent):
        self.apartment = apartment
        self.__monthly_rent = monthly_rent

    def process(self):
        return [self.apartment, self.__monthly_rent, self.__monthly_rent * 12]
    
#save to csv

Services = [
    Iqama("Ali", 2026, 750),
    Invoice("T-shirt", 100, 3, 0.15),
    Housing("Apartment-A", 3200)
] 

with open("Services.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Type", "Details"])
    for s in Services:
        writer.writerow([s.__class__.__name__, s.process()])


#save to Text File:
with open("Services_log.txt", "w") as f:
    for s in Services:
        f.write(f"{s.__class__.__name__} Processed: {s.process()}\n")

#Read Back From csv

with open("Services.csv", "r") as f:
    reader = csv.reader(f)
    print("CSV Data:")
    for row in reader:
        print(row)

#Read Back from Txt File:

with open("Services_log.txt", "r") as f:
    print("\nText File:")
    print(f.read())




    
