def zero(op = None):
    if op == None:
        return 0
    else:
        return op(0)
def one(op = None):
    if op == None:
        return 1
    else:
        return op(1)
def two(op = None):
    if op == None:
        return 2
    else:
        return op(2)
def three(op = None):
    if op == None:
        return 3
    else:
        return op(3)
def four(op = None):
    if op == None:
        return 4
    else:
        return op(4)
def five(op = None):
    if op == None:
        return 5
    else:
        return op(5)
def six(op = None):
    if op == None:
        return 6
    else:
        return op(6)
def seven(op = None):
    if op == None:
        return 7
    else:
        return op(7)
def eight(op = None):
    if op == None:
        return 8
    else:
        return op(8)
def nine(op = None):
    if op == None:
        return 9
    else:
        return op(9)

def plus(numb):
    return lambda x: x + numb
def minus(numb):
    return lambda x: x - numb
def times(numb):
    return lambda x: x * numb
def divided_by(numb):
    return lambda x: x // numb

