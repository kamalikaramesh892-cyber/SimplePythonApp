# Student Management System - Feature Version with Grade Calculation

class Student:
    def __init__(self):
        self.student_id = 0
        self.name = ""
        self.marks = 0
        self.grade = ""

    def set_details(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            self.grade = "A"
        elif self.marks >= 75:
            self.grade = "B"
        elif self.marks >= 60:
            self.grade = "C"
        elif self.marks >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

    def display_details(self):
        print("Student ID     :", self.student_id)
        print("Student Name   :", self.name)
        print("Student Marks  :", self.marks)
        print("Student Grade  :", self.grade)


def main():
    print("---- Student Management System ----")

    s = Student()

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Student Marks: "))

    s.set_details(student_id, name, marks)

    print("\nStudent Details:")
    s.display_details()

    if marks >= 50:
        print("Result Status  : PASS")
    else:
        print("Result Status  : FAIL")


if __name__ == "__main__":
    main()
