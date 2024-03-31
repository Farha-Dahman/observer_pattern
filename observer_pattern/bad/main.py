from course import Course
from student import Student

def main():
    # Create courses
    math_course = Course("Math")
    programming_course = Course("Programming")

    # Create students
    student1 = Student("Sara")
    student2 = Student("Sami")

    # Add students to courses
    math_course.add_student(student1)
    math_course.add_student(student2)
    programming_course.add_student(student1)

    # Set courses availability
    math_course.set_available(True)
    programming_course.set_available(False)

if __name__ == "__main__":
    main()
