class College:
    # Class attribute
    location = "City University"

    # Constructor method (initializer)
    def __init__(self, name):
        # Instance attributes
        self.name = name
        self.students = []

    # Instance method to enroll a student
    def enroll_student(self, student):
        self.students.append(student)
        return f"{student.name} has been enrolled in {self.name}"

    # Instance method to get the total number of students
    def total_students(self):
        return len(self.students)


class Student:
    # Constructor method (initializer)
    def __init__(self, name, age, major):
        # Instance attributes
        self.name = name
        self.age = age
        self.major = major

    # Instance method to display student details
    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}"


# Creating an instance of the College class
college = College("Engineering College")

# Creating instances of the Student class
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 21, "Electrical Engineering")

# Enrolling students to the college
print(college.enroll_student(student1))  # Output: Alice has been enrolled in Engineering College
print(college.enroll_student(student2))  # Output: Bob has been enrolled in Engineering College

# Getting the total number of students in the college
print(college.total_students())  # Output: 2

# Displaying student details
print(student1.display_details())  # Output: Name: Alice, Age: 20, Major: Computer Science
print(student2.display_details())  # Output: Name: Bob, Age: 21, Major: Electrical Engineering

# Accessing class attribute
print(college.location)  # Output: City University
