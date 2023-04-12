result=[1, 2, 3, 0, 5+5j, True, False, 3.56]


#filter syntax : filter(Function Name, Iteratable)
result1=list(filter(None, result))
result2=tuple(filter(None, result))
result3=set(filter(None, result))


print(result1)
print(result2)
print(result3)

