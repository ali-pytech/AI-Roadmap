"""Iqama Class Example"""


class iqama():
    def __init__(self, name, year, fee):
        self.name = name
        self.year = year
        self.fee = fee

    def display(self):
        return f"{self.name}  -  {self.year}  -   {self.fee}"
    
ali = iqama("Ali", 2026, 800)
ahmed = iqama("Ahmed", 2025, 750)

print("Iqama Record:")
print(ali.display())
print(ahmed.display())
