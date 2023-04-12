result=[1, 2, 3, 0, 5+5j, True, False, 3.56,"Python Programming","Machine Learning"]


#filter syntax : filter(Function Name, Iteratable)
result1=list(filter(None, result))
result2=tuple(filter(None, result))
result3=set(filter(None, result))
print(result1)
print(result2)
print(result3)

# filter with user defined function
#filter only integers from given list
result=[1, 2, 3, 9, 5+5j, True, False, 3.56,"Python Programming","Machine Learning"]
def filterdata(x):
    if type(x)==int:
        if x%3==0:
            return x
result4=list( filter(filterdata,result))
print(result4)


