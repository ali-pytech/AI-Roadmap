"""Student Abstraction"""

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        return "Student"
    
class Teacher(Person):
    def role(self):
        return "Teacher"
    
ali =Student()
ahmed = Teacher()

print("Ali:", ali.role())
print("Ahmed:", ahmed.role())
