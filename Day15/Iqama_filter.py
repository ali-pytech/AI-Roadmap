"""Iqama Renewal Filter"""

iqama = {
    "Ali": {"year":2026, "Fee":850, "Status": "Active"},
    "Ahmed":{"year":2025, "Fee":900, "Status": "Pending"},
    "Faisal":{"Year":2024, "Fee":950, "Status": "Expired"}   
}

print("Expired Iqama Records:")

for person , details in iqama.items():
    if details['Status'] == "Expired":
      print(f"Name : {person}: Fee {details['Fee']} SAR | Iqama Status : {details['Status']}")
