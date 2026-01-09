# Student Management System - Initial Version

class Student:
    def __init__(self):
        self.student_id = 0
        self.name = ""
        self.marks = 0

    def set_details(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display_details(self):
        print("Student ID     :", self.student_id)
        print("Student Name   :", self.name)
        print("Student Marks  :", self.marks)


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
