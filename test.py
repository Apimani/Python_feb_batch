import selectors


class Cal:
    "this is calculator class"
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Hello this is constructor")
        print('id of self', id(self))
    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

obj = Cal(4,3)

print(obj.add())

print(id(obj))

print(dir(Cal))

print(obj.__dict__)