
""""Iqama Encapsulation"""

class Iqama:
    def __init__(self, holder, year, fee):
        self.holder = holder
        self.year = year
        self.__fee = fee    #private attribute

    def get_fee(self):
        return self.__fee
    
    def set_fee(self, new_fee):
        if new_fee >0:
            self.__fee = new_fee

        else:
            print("Invalid fee")

ali = Iqama("Ali", 2025, 400)
print("Initail Fee:", ali.get_fee())
ali.set_fee(600)
print("Updated Fee:",ali.get_fee() )
