class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

class Classroom:
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name



carl = Student("Carl", "B", 12)
ms_francine = Classroom("Ms. Francine")

print(ms_francine.teacher_name)
print(type(ms_francine.teacher_name))