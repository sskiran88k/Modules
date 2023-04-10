import random as ran
Name1=input("Enter the First Name: ")
Name2=input("Enter the Second Name: ")

if(Name1==Name2):
    print("Both Names are equal")
else:
    y=ran.randint(1,100)
    print(f"The percentage of effection between two members: {y}")