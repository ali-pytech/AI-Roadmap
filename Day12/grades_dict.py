grades = {
    "Ali" : 86,
    "Ahmed" : 78,
    "Hamza" : 89,
    "Faisal" : 81
}

Average = sum(grades.values()) / len(grades)
highest_student = max(grades, key=grades.get)
print(f"Everage Garde: {Average}")
print(f"Highest Scorer: {highest_student} with {grades[highest_student]} Marks") 
