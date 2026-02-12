"""Student Record Check"""
students = {
    "Ali": {"age":23, "grade":"A", "major":"AI"},
    "Ahmed": {"Aage":24, "grade":"B+", "major":"Data Science"},
    "Faisal": {"age":25, "grade":"B", "major":"Cybersecurity"}
}
if "Ali" in students:
    print("Yes Ali is in Students Record")

else:
    print("Student Not Found in Record")
