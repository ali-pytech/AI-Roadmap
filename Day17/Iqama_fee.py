"""Iqama Fee Calcultor"""

def calculate_fee(year,base_fee):
    if year >= 2026:
        return base_fee * 1.10    #10% increment each year after 2026
    

    else:
        return base_fee
    
print(f"Ali's Fee : {calculate_fee(2026,800)} SAR")
print(f"Ahmed's Fee: {calculate_fee(2024,700)} SAR")
