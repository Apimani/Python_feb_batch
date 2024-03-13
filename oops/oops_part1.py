#Syntax

# class Class_name:
#     def __init__(self): # this construtor and const name always __init__, it is optional, self is current object memory
#         stmt1 # print stmt or logical code
#     def fun1(self): # instance method, it is optiona
#         stmt3 # print stmt or logical code
#     @classmethod
#     def fun2(cls): # class method, it is optional
#         stmt5 # print stmt or logical code
#
#     @staticmethod
#     def fun3(): # static method, it is optional
#         stmt7 # print stmt or logical code



# class Calculator:
#     """ this calculator class"""
#     def __init__(self):
#         print("This is constructor")
#     def add(self,a,b):
#         print("sum of two numbers", a+b)
#     def sub(self,a,b):
#         print("sub of two numbers", a-b)
#
#     def mul(self, a, b):
#         print("mul of two numbers", a * b)
#
# obj = Calculator() # object creation syntax ref_var_name = classname()
#
# obj2 = Calculator()
#
# obj3 = Calculator()
#
# obj.add(4,5)
# obj.sub(4,9)


class Calculator:
    """ this calculator class"""
    def __init__(self,a,b):
        print("This is constructor")
        print("Memory of self", id(self))
        self.a=a
        self.b=b
    def add(self):
        print("sum of two numbers", self.a+self.b)
    def sub(self):
        print("sub of two numbers", self.a-self.b)

obj = Calculator(4,5) # it will start with constrcutor execution and create memory for self and assign variables to self

obj.add()
obj.sub()
print(obj.a)
print(obj.b)

print(dir(Calculator))

print(Calculator.__doc__)
print(obj.__dict__)

obj2 = Calculator(40,50)
obj2.add()
obj2.sub()



