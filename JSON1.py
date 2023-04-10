import json
# JSON string
employee_dict = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(employee_dict))
print("\nNow Convert from Python to JSON")
# Convert Python dict to JSON
print(type(json.dumps(employee_dict, indent=4)))
print(f"Converted from Python to JSON:  \n {json.dumps(employee_dict, indent=4)}")