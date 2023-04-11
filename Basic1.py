import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York", "Distance":12.7}'

print(type(x))

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["Distance"])

print(type(y))
