
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
def calculator(a,b,):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    pow = a**b
    print(f"sum is {sum}, sub is {sub}, mul is {mul}, div is {div} and power is {pow}")

# calling calculator

calculator(10,20)
calculator(2,3)
calculator(4,-3)
calculator(100,2)


calculator(14,2)






