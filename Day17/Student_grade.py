"""Students Grade Function"""

def grade_status(score):
    if score>=90:
        return "Excellent"
    
    elif score >=70:
        return "Good"
    
    else:
        return "Need Improvements"
    
print(f"Ali : {grade_status(90)}")
print(f"Ahmed : {grade_status(78)}")
print(f"Faisal : {grade_status(66)}")
