import json
# JSON string
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(employee))
print("\nNow convert from JSON to Python")
print(type(json.loads(employee)))
print(f"Converted to Python: \n {json.loads(employee)}")