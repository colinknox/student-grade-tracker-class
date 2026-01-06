class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

class Classroom:
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name
        self.students_in_class = []

    def add_student(self, student):
        self.students_in_class.append(student)

    def remove_student(self, student):
        updated_student_list = []

        for current_student in self.students_in_class:

            if current_student.name != student.name and current_student.age != student.age:
                updated_student_list.append(current_student)

        self.students_in_class = updated_student_list

        return self.students_in_class

    def find_by_grade(self, grade):
        students_with_grade = []
        
        for current_student in self.students_in_class:
            if current_student.grade == grade:
                students_with_grade.append(current_student)

        return students_with_grade
    
    def search_students(self, search_string):
        students_in_search = []
        
        for current_student in self.students_in_class:
            if search_string in current_student.name:
                students_in_search.append(current_student)

        return students_in_search



classroom = Classroom("Mr. Smith")
classroom.add_student(Student("Alice", "A", 16))
classroom.add_student(Student("Bob", "B", 17))
classroom.add_student(Student("Charlie", "A", 16))

print(classroom.find_by_grade("a"))  # Should return Alice and Charlie
print(classroom.search_students("li"))  # Should return Alice and Charlie