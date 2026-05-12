"""Iqama Inheritance"""

class Document:
    def __init__(self, holder, year):
        self.holder = holder
        self.year = year

    def info(self):
        return f"Document For {self.holder} | Year: {self.year}"  
    

class Iqama(Document):
    def __init__(self, holder, year, fee):
        super().__init__(holder, year)
        self.fee = fee

    def info(self):
        return f"Iqama For {self.holder} | Year: {self.year} | Fee: {self.fee} SAR"
    
ali =Iqama("Ali", 2026, 650)
print(ali.info())
