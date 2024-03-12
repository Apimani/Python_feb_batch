# def fun1(num):
#     print(num)
#     return num + 25
#
# print(fun1(5))
# print(num)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def greeting(name):
    print("GM ", name)
    return 1

res1 = greeting('sreeni')
print(res1)

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
        return 4
    return a,inner_fun(a,b)
    return inner_fun(a, b)
    return a
    return b

result = outer_fun(5, 10)
print(result)

def display_person(*args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")