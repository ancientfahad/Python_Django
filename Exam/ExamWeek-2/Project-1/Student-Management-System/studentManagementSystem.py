"""
Author: Al Fahad Chowdhury
Date: 1 Nov, 2024

Course: Full Stack Web Development with Python, Django & React
Batch: 2
Module: 10
Project Name: Student Management System

Project Description: This project is a command-line interface Student Management System that allows users to manage student records, 
course enrollments, and grade assignments. The system provides functionalities to add new students, add new courses, 
enroll students into courses, assign grades, and display student and course details. It also includes error handling for 
invalid inputs and operations. Data can be saved to and loaded from a JSON file, enabling persistent storage across sessions.

"""

import json

# Define a base Person class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Define the Student class inheriting from Person
class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "student_id": self.student_id,
            "grades": self.grades,
            "courses": self.courses
        }

# Define the Course class
class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def to_dict(self):
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "students": [student.student_id for student in self.students]
        }

# Define the main Student Management System class
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, name, age, address, student_id):
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self, course_name, course_code, instructor):
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course:
            student.courses.append(course.course_name)
            course.students.append(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course.course_code}).")
        else:
            print("Error: Student or Course not found.")

    def add_grade_for_student(self, student_id, course_code, grade):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course and course.course_name in student.courses:
            student.grades[course.course_name] = grade
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")
        else:
            print("Error: Student not enrolled in course or invalid ID/Course Code.")

    def display_student_details(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Address: {student.address}")
            print(f"Courses: {', '.join(student.courses)}")
            print(f"Grades: {student.grades}")
        else:
            print("Error: Student ID not found.")

    def display_course_details(self, course_code):
        course = self.courses.get(course_code)
        if course:
            print(f"Course Name: {course.course_name}")
            print(f"Instructor: {course.instructor}")
            print("Students:", ', '.join([s.name for s in course.students]))
        else:
            print("Error: Course Code not found.")

    def save_data(self):
        data = {
            "students": {sid: s.to_dict() for sid, s in self.students.items()},
            "courses": {cid: c.to_dict() for cid, c in self.courses.items()}
        }
        with open("/Users/u75530/Documents/GitHub/Python_Django/Module-10/Project-1/Student-Management-System/studentmanagementsystem.json", 'w') as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open("/Users/u75530/Documents/GitHub/Python_Django/Module-10/Project-1/Student-Management-System/studentmanagementsystem.json", 'r') as file:
                data = json.load(file)
                for sid, s_data in data["students"].items():
                    student = Student(s_data['name'], s_data['age'], s_data['address'], sid)
                    student.grades = s_data.get('grades', {})
                    student.courses = s_data.get('courses', [])
                    self.students[sid] = student
                for cid, c_data in data["courses"].items():
                    course = Course(c_data['course_name'], c_data['course_code'], c_data['instructor'])
                    course.students = [self.students[sid] for sid in c_data.get('students', [])]
                    self.courses[cid] = course
        except FileNotFoundError:
            print("No data file found.")
        except json.JSONDecodeError:
            print("Error in data file format.")

    def show_json_data(self):
        try:
            with open("/Users/u75530/Documents/GitHub/Python_Django/Module-10/Project-1/Student-Management-System/studentmanagementsystem.json", 'r') as file:
                data = json.load(file)
            print(json.dumps(data, indent=4))
        except FileNotFoundError:
            print("No data file found.")
        except json.JSONDecodeError:
            print("Error in data file format.")

# Function to run the CLI
def main_menu():
    system = StudentManagementSystem()

    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")

        option = input("\nSelect Option: ")
        
        if option == "1":
            print("\n--- Add New Student ---")

            # Validate name input
            while True:
                name = input("Enter Name: ").strip()
                if name:
                    break
                else:
                    print("Error: Name is required.")

            # Validate age input
            while True:
                try:
                    age = int(input("Enter Age: ").strip())
                    if age > 0:
                        break
                    else:
                        print("Error: Age must be a positive integer.")
                except ValueError:
                    print("Error: Invalid age. Please enter a number.")

            # Validate address input
            while True:
                address = input("Enter Address: ").strip()
                if address:
                    break
                else:
                    print("Error: Address is required.")

            # Validate student ID input
            while True:
                student_id = input("Enter Student ID: ").strip()
                if student_id:
                    break
                else:
                    print("Error: Student ID is required.")

            print()  # Space before output
            system.add_student(name, age, address, student_id)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "2":
            print("\n--- Add New Course ---")

            # Validate course name
            while True:
                course_name = input("Enter Course Name: ").strip()
                if course_name:
                    break
                else:
                    print("Error: Course Name is required.")

            # Validate course code
            while True:
                course_code = input("Enter Course Code: ").strip().upper()
                if course_code:
                    break
                else:
                    print("Error: Course Code is required.")

            # Validate instructor name
            while True:
                instructor = input("Enter Instructor Name: ").strip()
                if instructor:
                    break
                else:
                    print("Error: Instructor Name is required.")

            print()  # Space before output
            system.add_course(course_name, course_code, instructor)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "3":
            print("\n--- Enroll Student in Course ---")

            # Validate student ID
            while True:
                student_id = input("Enter Student ID: ").strip()
                if student_id:
                    break
                else:
                    print("Error: Student ID is required.")

            # Validate course code
            while True:
                course_code = input("Enter Course Code: ").strip().upper()
                if course_code:
                    break
                else:
                    print("Error: Course Code is required.")

            print()  # Space before output
            system.enroll_student_in_course(student_id, course_code)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "4":
            print("\n--- Add Grade for Student ---")

            # Validate student ID
            while True:
                student_id = input("Enter Student ID: ").strip()
                if student_id:
                    break
                else:
                    print("Error: Student ID is required.")

            # Validate course code
            while True:
                course_code = input("Enter Course Code: ").strip().upper()
                if course_code:
                    break
                else:
                    print("Error: Course Code is required.")

            # Validate grade input
            while True:
                grade = input("Enter Grade: ").strip().upper()
                if grade in ["A", "B", "C", "D", "F"]:
                    break
                else:
                    print("Error: Grade must be one of A, B, C, D, F.")

            print()  # Space before output
            system.add_grade_for_student(student_id, course_code, grade)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "5":
            print("\n--- Display Student Details ---")
            
            # Validate student ID
            while True:
                student_id = input("Enter Student ID: ").strip()
                if student_id:
                    break
                else:
                    print("Error: Student ID is required.")

            print()  # Space before output
            system.display_student_details(student_id)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "6":
            print("\n--- Display Course Details ---")
            
            # Validate course code
            while True:
                course_code = input("Enter Course Code: ").strip().upper()
                if course_code:
                    break
                else:
                    print("Error: Course Code is required.")

            print()  # Space before output
            system.display_course_details(course_code)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "7":
            print("\n--- Save Data to File ---")
            print()  # Space before output
            system.save_data()
            print("\nAll student and course data saved successfully.")
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "8":
            print("\n--- Load Data from File ---")
            print()  # Space before output
            system.load_data()
            print("\nData loaded successfully.")
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "0":
            print("\nExiting Student Management System. Goodbye!")
            break

        elif option == "99":
            print("\n--- Display JSON Data ---")
            print()  # Space before output
            system.show_json_data()
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        else:
            print("\nInvalid option. Please try again.")
            input("Press Enter to continue...")  # Pause here if invalid option is selected

# Run the CLI
if __name__ == "__main__":
    main_menu()