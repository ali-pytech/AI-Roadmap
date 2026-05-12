"""Student Polymorphism"""

class Person:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "General Person"
    
class Student(Person):
    def role(self):
        return "Student"
    
class Teacher(Person):
    def role(self):
        return "Teacher"
    
ali = Student("Ali")
ahmed = Teacher("Ahmed")

print(ali.name, "|" , ali.role())
print(ahmed.name, "|", ahmed.role())
