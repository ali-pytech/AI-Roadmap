"""Student Grade Input"""
def grade_input():
    try:
        score = int(input("Enter Your Score: "))
        return score
    
    except ValueError:
        print("Invalid Input! please Enter Only Numbers!")

print("Score: ",grade_input())
