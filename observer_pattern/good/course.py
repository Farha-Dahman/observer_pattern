# Subject (Observable)
class Course:
    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []
        self.__available = False

    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def get_students(self):
        return self.__students

    def add_student(self, student):
        self.__students.append(student)
        print(f"Student {student.get_student_name()} added to course {self.__course_name}")

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            print(f"Student {student.get_student_name()} removed from course {self.__course_name}")
        else:
            print(f"Student {student.get_student_name()} is not enrolled in course {self.__course_name}")

    def is_available(self):
        return self.__available

    def set_available(self, available):
        self.__available = available
        if available:
            self.notify_students(f"{self.__course_name} course is now available")
        else:
            self.notify_students(f"{self.__course_name} course is unavailable")

    def notify_students(self, message):
        for student in self.__students:
            student.notify(message)
