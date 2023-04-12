from functools import reduce
a=[1, 2, 4, 6, 8, 13, 16, "Happy Programming", 3.4, 9.3, True, False]
print(a )
def even(x):
    if type(x)==int:
        if x%2==0:
            return x
y=list(filter(even,a))
print(y)

def square(x):
    return x*x
z=list(map(square,y))
print(z)

def addition(a,b):
    return a+b
print(reduce(addition, z))



