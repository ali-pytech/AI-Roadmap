"""Everage Grade Calculator"""

students = { 
    "Ali": {"grade": 90}, 
    "Faisal": {"grade": 85}, 
    "Ahmed": {"grade": 78} 
    
}

total = 0
for name , details in students.items():
    total += details['grade']

everage = total / len(students)
print(f"Everage Grade: {everage:.2f}")
