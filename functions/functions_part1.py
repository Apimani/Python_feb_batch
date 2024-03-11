#
# #project-->package-->module file(.py)--> class --> function/method
#
# # what is function?
# # piece of code which does repetative task
#
# #syntax:
#
# #def function_name(args): # args optional
#     #repetative task( python stmts)
#     # return stmt ( optional )
#
#
# # Function definition
# def greeting(name):
#     if name=='Sreeni':
#         print(f"Hello {name}, Good Afternoon, How are you?")
#     else:
#         print(f"Hello {name}, Good Afternoon")
#
#
# # function call
# greeting('ETL')
# greeting('Sreeni')
# greeting('ETL2')
#
# # generate_number function definition
# def generate_number(start, end):
#     for i in range(start, end):
#         print(i)
#
# # call generate_number function
# generate_number(1,10)
# print("#"*50)
# generate_number(1,10)
# print("#"*50)
# generate_number(5,20)
# print("#"*50)
# generate_number(2,5)
# print("#"*50)
# generate_number(100,103)
# print("#"*50)

# definition
# def calculator(a,b):
#     sum = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     pow = a**b
#     print(f"sum is {sum}, sub is {sub}, mul is {mul}, div is {div} and power is {pow}")
#
# # calling calculator
#
# calculator(10,20)
# calculator(2,3)
# calculator(4,-3)
# calculator(100,2)
#
#
# calculator(14,2)

# bit bucket, github, ADO( git language)

# def add(a, b):
#     # print(f"Sum of {a} and {b} is {a + b}")
#     return a + b
#
#
# add_out2 = add(a=4, b=5)
# print("add_out2", add_out2)
# add_out = add(3, 4)
# print("add_out", add_out)
#
# add_out3 = add(10, 40)
# print("add_out3", add_out3)


def calc(a, b, c, d=0):
    print("a values", a)
    print("b values", b)
    print("c values", c)
    print("d values", d)
    add_of_all = a + b + c + d
    return add_of_all


# print(calc(10,20,30,130)) #10,20,30,50 --> positional arguments
# out = calc(40,20,30,130) #10,20,30,50 --> positional arguments
# print("out", out)
# print(calc(a=10, b=20, c=30, d=50))  # a=10, b=20, c=30, d=50 --> keyword argument
# print(calc(b=20, a=10, d=50, c=30))
#
# print(calc(b=20, a=10, c=30,d=200))

print(calc(10,20,c=40,d=50))
print(calc(10,20,40,d=50))
print(calc(a=20,b=30,c=50,d=100)) # first give all positional, keyword, default
print(calc(20,30,c=50,d=100)) # first give all positional, keyword, default
