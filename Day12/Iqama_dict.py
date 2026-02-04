"""Iqama Dictionary"""
iqama = {
    "Ali": {"year":2026, "fee": 800},
    "Ahmed": {"year":2025, "fee":750},
    "Faisal": {"year":2024, "fee":600}

}

for person,details in iqama.items():
    print(f"{person} - Renewal Year: {details["year"]} and Fee is {details["fee"]} SAR") 
