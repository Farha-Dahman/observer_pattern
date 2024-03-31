# Observer
class Student:
    def __init__(self, student_name):
        self.__student_name = student_name

    def get_student_name(self):
        return self.__student_name

    def set_student_name(self, student_name):
        self.__student_name = student_name

    def notify(self, message):
        print(f"Notification for {self.__student_name}: {message}")
