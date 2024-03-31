class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        self.available = False

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.student_name} added to course {self.course_name}")

    def remove_student(self, student):
        self.students.remove(student)
        print(f"Student {student.student_name} removed from course {self.course_name}")

    def set_available(self, available):
        self.available = available
        if available:
            for student in self.students:
                student.notify(f"{self.course_name} course is now available")
        else:
            for student in self.students:
                student.notify(f"{self.course_name} course is unavailable")
