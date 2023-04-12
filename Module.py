import calculator as cal

while True:
    choice= input("Enter your choice")
    if choice=='1':
        a,b=eval(input("Enter the numbers to add"))
        print(f"the addition of two numbers is {cal.add(a,b)}")
    if choice=='2':
        a,b=eval(input("Enter the numbers to subtract"))
        print(f"the subtraction of two numbers is {cal.sub(a,b)}")
    if choice=='3':
        a,b=eval(input("Enter the numbers to multiply"))
        print(f"the multiplication of two numbers is {cal.mul(a,b)}")
    if choice=='Q':
        break
            
    



