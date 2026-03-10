
class GradeError(Exception):
    pass

def create_student_record(name, score):
    if not ( 0<= score <= 100):
        raise GradeError ("Score Should be Between 0 to 100")
    
    if score >= 90:
        status = "Excellent"
    
    elif score >=75:
        status = "Good"

    else:
        status =  "Need Improvement"

    return {"Name": name , "Score": score , "Status": status}

try:
    ali = create_student_record("Ali",90)
    ahmed = create_student_record("Ahmed",125)   #invalid
    students = [ali , ahmed]

    print("Student Record:", students)

except GradeError as g:
    print("Error:",g)
