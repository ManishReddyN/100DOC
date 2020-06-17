def cons(a, b):
    def pair(f):
        return sumi(a, b)
    return pair
def sumi(a,b):
        return a+b
def car(f):
    def left(a,b):
        return a
    return f(left)
# print(car(cons(3,4)))
print(cons(3,4))