
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
