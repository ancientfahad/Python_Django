"""
Author: Al Fahad Chowdhury
Date: 15 Sep, 2024

Course: Full Stack Web Development with Python, Django & React
Batch: 2
Module: 10
Project: 1
Project Name: Student Management System

Project Description: This project is a command-line Student Management System that allows users to manage student records, 
course enrollments, and grade assignments. The system provides functionalities to add new students, create courses, 
enroll students in courses, assign grades, and display student and course details. It also includes error handling for 
invalid inputs and operations. Data can be saved to and loaded from a JSON file, enabling persistent storage across sessions.

Variables:

- choice: Stores the user's selected operation (1-8).
- name, age, address, student_id: Information collected for adding new students.
- course_name, course_code, instructor: Information collected for creating new courses.
- student_id, course_code, grade: Information used for enrolling students and assigning grades.
- filename: Used to specify the file for saving or loading data.

Classes:

- Person: Represents a generic person with attributes like name, age, and address, including a method to display personal information.
- Student: Inherits from Person and adds student-specific attributes (student_id, grades, courses) and methods for managing grades and course enrollments.
- Course: Represents a course with attributes such as course_name, course_code, instructor, and a list of enrolled students, including a method to display course details.
- StudentManagementSystem: Manages all student and course operations, including adding students and courses, enrolling students, assigning grades, and handling data persistence.

Functions:
- add_student(name, age, address, student_id): Creates a new Student object and adds it to the system.
- add_course(course_name, course_code, instructor): Creates a new Course object and adds it to the system.
- enroll_student_in_course(student_id, course_code): Enrolls a specified student in a specified course.
- add_grade_for_student(student_id, course_code, grade): Assigns or updates a grade for a student in a specified course.
- display_student_details(student_id): Displays detailed information for a specified student.
- display_course_details(course_code): Displays detailed information for a specified course.
- save_data(filename): Saves all student and course data to a specified JSON file.
- load_data(filename): Loads student and course data from a specified JSON file.
- main_menu(): Main function that handles user interactions through a menu-driven interface, allowing users to perform various operations until they choose to exit.
"""

import json

# Custom JSON encoder for serializing objects of custom classes
class StudentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {
                'name': obj.name,
                'age': obj.age,
                'address': obj.address,
                'student_id': obj.student_id,
                'grades': obj.grades,
                'courses': obj.courses
            }
        elif isinstance(obj, Course):
            return {
                'course_name': obj.course_name,
                'course_code': obj.course_code,
                'instructor': obj.instructor,
                'students': [student.student_id for student in obj.students]
            }
        return super().default(obj)

# Class representing a person with basic attributes and method to display info
class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        """Displays the personal information of the person."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

# Class representing a student that inherits from Person
class Student(Person):
    def __init__(self, name: str, age: int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}  # Dictionary to store grades
        self.courses = []  # List to store enrolled courses

    def add_grade(self, subject: str, grade: str):
        """Adds or updates the grade for a specified subject."""
        self.grades[subject] = grade

    def enroll_course(self, course: str):
        """Enrolls the student in a specified course."""
        self.courses.append(course)

    def display_student_info(self):
        """Displays all details of the student."""
        print(f"Student Information:")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Enrolled Courses: {', '.join(self.courses)}")
        print(f"Grades: {self.grades}")

# Class representing a course
class Course:
    def __init__(self, course_name: str, course_code: str, instructor: str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []  # List to store enrolled students

    def add_student(self, student: Student):
        """Adds a student to the course."""
        self.students.append(student)

    def display_course_info(self):
        """Displays course details and the list of enrolled students."""
        print(f"Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join(student.name for student in self.students)}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to hold students by their ID
        self.courses = {}   # Dictionary to hold courses by their code

    def add_student(self, name: str, age: int, address: str, student_id: str):
        """Creates a new Student object and adds it to the system."""
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self, course_name: str, course_code: str, instructor: str):
        """Creates a new Course object and adds it to the system."""
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self, student_id: str, course_code: str):
        """Enrolls a student in a specified course."""
        student = self.students.get(student_id)
        course = self.courses.get(course_code)

        if student and course:
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Error: Student ID or Course Code not found.")

    def add_grade_for_student(self, student_id: str, course_code: str, grade: str):
        """Assigns or updates the grade for the student in the specified course."""
        student = self.students.get(student_id)
        course = self.courses.get(course_code)

        if student and course and course.course_name in student.courses:
            student.add_grade(course.course_name, grade)
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")
        else:
            print("Error: Student not enrolled in this course or invalid ID/Course Code.")

    def display_student_details(self, student_id: str):
        """Displays the details of a specified student."""
        student = self.students.get(student_id)
        if student:
            student.display_student_info()
        else:
            print("Error: Student ID not found.")

    def display_course_details(self, course_code: str):
        """Displays the details of a specified course."""
        course = self.courses.get(course_code)
        if course:
            course.display_course_info()
        else:
            print("Error: Course Code not found.")

    def save_data(self):
        """Saves all student and course data to 'studentmanagementsystem.json' in JSON format."""
        data = {
            "students": self.students,
            "courses": self.courses
        }
        with open("studentmanagementsystem.json", 'w') as file:
            json.dump(data, file, cls=StudentEncoder)
        print("All student and course data saved to 'studentmanagementsystem.json' successfully.")

    def load_data(self):
        """Loads data from 'studentmanagementsystem.json', restoring student and course information."""
        try:
            with open("studentmanagementsystem.json", 'r') as file:
                data = json.load(file)
                # Deserialize students
                for student_id, student_data in data["students"].items():
                    student = Student(
                        student_data['name'],
                        student_data['age'],
                        student_data['address'],
                        student_data['student_id']
                    )
                    student.grades = student_data['grades']
                    student.courses = student_data['courses']
                    self.students[student_id] = student
                # Deserialize courses
                for course_code, course_data in data["courses"].items():
                    course = Course(
                        course_data['course_name'],
                        course_data['course_code'],
                        course_data['instructor']
                    )
                    course.students = [self.students[student_id] for student_id in course_data['students']]
                    self.courses[course_code] = course
            print("Data loaded from 'studentmanagementsystem.json' successfully.")
        except FileNotFoundError:
            print("Error: 'studentmanagementsystem.json' not found.")
        except json.JSONDecodeError:
            print("Error: Data file is corrupt.")

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
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            print()  # Space before output
            system.add_student(name, age, address, student_id)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here
        
        elif option == "2":
            print("\n--- Add New Course ---")
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            print()  # Space before output
            system.add_course(course_name, course_code, instructor)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here
        
        elif option == "3":
            print("\n--- Enroll Student in Course ---")
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            print()  # Space before output
            system.enroll_student_in_course(student_id, course_code)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here
        
        elif option == "4":
            print("\n--- Add Grade for Student ---")
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            print()  # Space before output
            system.add_grade_for_student(student_id, course_code, grade)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here
        
        elif option == "5":
            print("\n--- Display Student Details ---")
            student_id = input("Enter Student ID: ")
            print()  # Space before output
            system.display_student_details(student_id)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here
        
        elif option == "6":
            print("\n--- Display Course Details ---")
            course_code = input("Enter Course Code: ")
            print()  # Space before output
            system.display_course_details(course_code)
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here
        
        elif option == "7":
            print("\n--- Save Data to File ---")
            print()  # Space before output
            system.save_data()
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here

        elif option == "8":
            print("\n--- Load Data from File ---")
            print()  # Space before output
            system.load_data()
            print()  # Space after output
            input("Press Enter to continue...")  # Pause here
                
        elif option == "0":
            print("\nExiting Student Management System. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")
            input("Press Enter to continue...")  # Pause here if invalid option is selected

# Run the CLI
if __name__ == "__main__":
    main_menu()