from functools import reduce
c=[3, 6, 9]
print(c)
def product(x,y):
    print(f"the value of x is : {x}")
    print(f"the value of y is : {y}")
    z=x*y
    print(f"the value of z is : {z}")
    return z

result=reduce(product,c)



print(result)
