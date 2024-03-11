#
# def cal(a,b):
#     addition = a+b
#     mul = a*b
#     print(f"Sum of {a} and {b} is {addition}")
#     print(f"multiplication of {a} and {b} is {mul}")
#     return addition, mul
#
# #print(cal(10,20))
#
# def cal(a,b,c):
#     addition = a+b+c
#     mul = a*b*c
#     print(f"Sum of {a} , {b} and {c}is {addition}")
#     print(f"multiplication of {a} , {b} and {c} is {mul}")
#     return addition, mul

#print(cal(10,20,40))

#print(cal(10,20))
# def cal(*args):
#     addition = 0
#     mul = 1
#     print("type of args",type(args))
#     print("args", args)
#     for i in args:
#         addition = addition+i
#         mul = mul*i
#     print(f"Sum of {args} is {addition}")
#     print(f"multiplication of {args} is {mul}")
#     return addition, mul
#
# cal(10,20,30,40)
# cal(10,20)
# cal(10)
# cal(10,20,30,40,50,60,70)
# cal()
#
# def cal(**kwargs):
#     print("type of kwargs", type(kwargs))
#     print("kwargs values", kwargs)
#     sum=0
#     mul=1
#     for value in kwargs.values():
#         sum=sum+value
#         mul=mul*value
#
#     print(f"Sum of {kwargs.values()} is {sum}")
#     print(f"multiplication of {kwargs.values()} is {mul}")
#     return sum, mul
#
# cal(g=20,f=30)
# cal(g=20,f=30,a=50)
# cal(g=20,f=30,a=50, c=40, d=10, k=1)

def cal(a,*args,b, default1=20):
    sum = 0
    for i in args:
        sum = sum+i
    sum = sum+a+b+default1
    print(f"Sum of {args,a,b,default1} is {sum}")
    return sum

cal(10,5,10,20,30, b=40 ,default1=50)













































#
# def cal(a,b,c):
#     addition = a+b+c
#     sub = a-b-c
#     mul = a*b*c
#     print(f"Sum of {a} , {b}, {c} is {addition}")
#     print(f"sub of {a} , {b},{c} is {sub}")
#     print(f"multiplication of {a} , {b}, {c} is {mul}")
#     return addition,sub, mul
#
# cal(10,20,30)


# def cal(*args):
#     print(type(args))
#     print(args)
#     sum = 0
#     mul = 1
#     for i in args:
#         sum = sum+i
#         mul = mul * i
#     print(f"The sum of {args} values is", sum)
#     print(f"The mul of {args} values is", mul)
#
# cal(10,20.0)
# cal(10,20)
# cal(10,20,33)
# cal(10,20,33,55,76,99)
# cal(10,2)

# def cal2(**kwargs):
#     #print(type(args))
#     #print(args)
#     #print("args.get('a')",args.get('a'))
#     sum = 0
#
#     for value in kwargs.values():
#         sum = sum+value
#
#     # for key, value in kwargs.items():
#     #     sum = sum + value
#     print(f"Sum of {kwargs.values()}", sum)
#
# cal2(a=10,b=20,c=30,d=40,e=400,f=200)
#
# cal2(k=100,l=120,m=130,n=140,o=4,p=2)