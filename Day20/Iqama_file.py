"""Iqama Records Text File"""


records = [
    {"name": "Ali", "year": 2026, "fee": 800},
    {"name": "Ahmed", "year": 2025, "fee": 750}
]


with open("iqama.txt", "w") as file:
    for record in records:
        file.write(f"{record['name']}  -  {record['year']} -  {record['fee']}")

with open("iqama.txt", "r") as file:
    data = file.read()
    print("Iqama File Content:\n",data)
