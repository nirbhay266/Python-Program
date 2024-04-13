x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
ao=input("Enter Airthmetic Operator: ")
if ao=="+":
    print("Addition is",x+y)
elif ao=="-":
    print("Substraction is",x-y)
elif ao=="*":
    print("Multiplication is",x*y)
elif ao=="/":
    print("Division is",x/y)
elif ao=="%":
    print("Modulus is",x%y)
else:
    print("Invalid Operator")
     