
import csv
import json
from abc import ABC,  abstractmethod


class Services(ABC):
    @abstractmethod
    def process(self):
        pass

class Iqama(Services):
    def __init__(self, holder, year, fee):
        self.holder = holder
        self.year = year
        self.__fee = fee

    def get_fee(self):
        return self.__fee
    
    def process(self):
        return {"Type": "Iqama" ,  "Holder": self.holder,  "Year": self.year,  "Fee": self.__fee}
    
class Invoice(Services):
    def __init__(self, item, price, quantity, vat_rate):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.vat_rate = vat_rate

    def process(self):
        total = self.price * self.quantity * (1 + self.vat_rate)
        return {"Type": "Invoice",  "Item": self.item,  "Price": self.price,  "Quantity": self.quantity,  "Total With VAT": total}
    

class Housing(Services):
    def __init__(self, apartment, monthly_rent):
        self.apartment = apartment
        self.__monthly_rent = monthly_rent

    def get_rent(self):
        return self.__monthly_rent
    
    def process(self):
        return {"Type": "Housing Record",  "Monthly Rent": self.__monthly_rent,  "Annual Rent": self.__monthly_rent * 12}
    

Documents = [
    Iqama("Ahmed", 2026, 750),
    Invoice("Laptop", 1700, 3, 0.15),
    Housing("Apartment-A", 2300)
]

#write to json
data =[d.process() for d in Documents]
with open("Documents.json", "w") as f:
    json.dump(data, f, indent=4)

#save to csv
with open("Documents.csv", "w", newline="") as f:
    writer=csv.DictWriter(f, fieldnames = ["Type", "Holder", "Year", "Fee", "Item", "Price", "Quantity", "Total With VAT", "Apartment", "Monthly Rent", "Annual Rent"])
    writer.writeheader()
    for record in data:
        writer.writerow(record)

#read back from json
with open("Documents.json", "r") as f:
    loaded_json = json.load(f)
    print("Json Data:", loaded_json)

#read back from csv
with open("Documents.csv", "r") as f:
    reader = csv.reader(f)
    print("\nCSV Data:")
    for row in reader:
        print(row)


    


