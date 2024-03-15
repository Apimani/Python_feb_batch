class College:

    college_location = 'BNG'  # class/static variable

    def __init__(self, name, rollno):
        self.name = name  # instance variable
        self.rollno = rollno  # instance variable
        self.age = 18
        del self.age
        College.college_name='AUTO' # class variable
        print(College.college_location)

    def student_info(self):  # if we use atleast one instance variable then we call method as instance method
        print("Student info is ", self.name, self.rollno, self.college_name, College.college_location)
        self.marks = 97  # instance variable
        del self.rollno
        College.college_owner = 'ABC' # class variable

    @classmethod
    def college_info(cls):  # not using any instance variables but using atleast ine class variable
        print("COllege name", cls.college_name)
        print("COllege name", College.college_name)
        cls.ECE_HOD = 'Dr. Arun'
        College.CSE_HOD = 'Dr. Avinash'


    @staticmethod
    def percentage(No_of_student, Failed_students):  # not using any of the instance/class variables
        if No_of_student > Failed_students:
            percentage = (Failed_students / No_of_student) * 100
            print("percentage", percentage)
        College.test= 'test'
        print(College.college_principle)

    college_principle = 'DR. AT' # class variable



obj = College('sreeni', 123)

print("immediate after object creation", obj.__dict__)
obj.student_info()

print("immediate after student_info execution", obj.__dict__)

obj.branch='ECE'
print("immediate after obj.branch execution", obj.__dict__)

print("Instance variable accessing out side of the class", obj.name)

del obj.name
print("immediate del obj.name execution", obj.__dict__)

obj.percentage()
print(College.__dict__)

print(obj.college_location)


