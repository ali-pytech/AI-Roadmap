"""Student Grades System"""
students = {
    "Ali": {"age":23, "grade":"A", "major":"AI"},
    "Ahmed": {"Aage":24, "grade":"B+", "major":"Data Science"},
    "Faisal": {"age":25, "grade":"B", "major":"Cybersecurity"}
}
 
for name, details in students.items():
    print(f"Student Name: {name} | Garde: {details['grade']} | Department: {details['major']}") 
