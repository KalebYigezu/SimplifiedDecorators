
def mod_div(func):
    def inner(a, b):
        if b == 0:
            print("You can not divide any number by zero")
        else:
            print(a/b)
    return inner

def div(a, b):
    print(a/b)
    
div = mod_div(div)

div(8, 0)

------------------ or -------------------

def mod_div(func):
    def inner(a, b):
        if b == 0:
            print("You can not divide any number by zero")
        else:
            print(a/b)
    return inner


@mod_div
def div(a, b):
    print(a/b)
    
    
div(8, 0)

--------------------------------------------
     Best Real Life Decorator Example 


def really_fine(func):
    def inner(*args, **kwargs):
        if args[0] > 100:
            print("Bro, don't be greedy")
        else:
            func(*args, **kwargs)

    return inner


@really_fine
def fine(num):
    print("Fine")


fine(101)
----------------------------------------------
           Class Decorator

class AddDec:
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        result=self.func(*args, **kwargs)
        return result * 2


@AddDec
def add(a, b):
    return a+b


print(add(2, 3))
