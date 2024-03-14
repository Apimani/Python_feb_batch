# class Student:
#     def __init__(self):
#         print("This is constructor")
#         print("Memory of self", id(self))
#
#
# obj = Student()
# print("obj memory", id(obj))
# obj2 = Student()
# print("obj2 memory", id(obj2))
# obj3 = Student()
# print("obj2 memory", id(obj3))


# class Student:
#     def __init__(kelf, rollno, name):
#         print("This is constructor")
#         print("Memory of kelf", id(kelf))
#         kelf.name = name
#         kelf.rollno = rollno
#     def student_display(kelf):  # if we use self as first argument then this fun is consider as instance method
#         print("The student name is", kelf.name)
#         print("Roll number", kelf.rollno)
#
#
#
# obj = Student(111,'test')
# print("obj memory", id(obj))
#
# print("obj.__dict__",obj.__dict__)
#
# obj.student_display()
#
# obj2 = Student(112,'test2')
#
# obj2.student_display()


# class Student:
#     college = 'SVU' # class variable
#     def __init__(self,name):
#         print("This is constructor")
#         self.name = name # instance variable, because this name value will change object to object
#
#     def student_dis(self):
#         print("Name of the student", self.name)
#
# obj = Student("sreeni")
#
# obj.student_dis()
# obj.student_dis()
# obj.student_dis()
#
#
# obj2 = Student("sreeni2")
#
# obj3 = Student("sreeni3")


class Student:
    def __init__(self):
        print("This is only self constructor")

    def __init__(self,name):
        print("This is self+name constructor")
        self.name = name # instance variable, because this name value will change object to object

    def __init__(self,name,rollno):
        print("This is selt+name+rollno constructor")
        self.name = name # instance variable, because this name value will change object to object
        self.rollno=rollno

    def student_dis(self,name):
        print("Name of the student", name)
        print(id(self))

obj = Student('test3',2)

obj.student_dis()

obj.student_dis()
obj.student_dis()
obj.student_dis()





def student_dis( name):
    print("Name of the student", name)



