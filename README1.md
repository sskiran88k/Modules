import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])
print(y["age"])
print(y["city"])



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


import json

x='{"Name": "SS Kiran","Mobile Number" : 9985163700,"College": "Lendi College","Adress":"Jonnada"}'

print(type(x))

y=json.loads(x)

print(y)
print(type(y))

y=json.dumps(x)
print(y)

print(type(y))


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(x)
print(type(x))
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))

import json
# JSON string
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(employee))
print("\nNow convert from JSON to Python")
print(type(json.loads(employee)))
print(f"Converted to Python: \n {json.loads(employee)}")

import json
# JSON string
employee_dict = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(employee_dict))
print("\nNow Convert from Python to JSON")
# Convert Python dict to JSON
print(type(json.dumps(employee_dict, indent=4)))
print(f"Converted from Python to JSON:  \n {json.dumps(employee_dict, indent=4)}")