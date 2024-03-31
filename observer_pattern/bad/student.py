class Student:
    def __init__(self, student_name):
        self.student_name = student_name

    def notify(self, message):
        print(f"Notification for {self.student_name}: {message}")
