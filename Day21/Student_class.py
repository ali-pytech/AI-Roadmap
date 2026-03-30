"""Student Class"""

class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def status(self):
        if self.score >= 90:
            return "Excellent"
        
        elif self.score >=75:
            return "Good"
        else:
            return "Need Improvement"
        
ali = student("Ali",92)
Ahmed = student("Ahmed",50)

print("Score Card")
print(ali.name, "--", ali.status())
print(Ahmed.name, "--", Ahmed.status())
