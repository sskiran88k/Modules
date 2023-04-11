import json

x='{"Name": "SS Kiran","Mobile Number" : 9985163700,"College": "Lendi College","Adress":"Jonnada"}'

print(type(x))

y=json.loads(x)

print(y)
print(type(y))

y=json.dumps(x)
print(y)

print(type(y))
