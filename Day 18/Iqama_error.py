"""Iqama Input Validation"""

def get_iqama_fee(year):
    try:
        fee = int(input("Enter Iqama Fee: "))
        return {'year':year, "fee": fee}
    
    except ValueError:
        print("Enter Only Numbers. Fee Must be in Numbers!!")


Record = get_iqama_fee(2025)
print("Record", Record)
