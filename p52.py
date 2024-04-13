"""(52) Write a program to enter two Numbers and also enter one Arithmetic 
 Operator then calculate the appropriate operation and finally print 
 the Result. if inputted Arithmetic operator is invalid then print 
 “Invalid Arithmetic Operator”.
 then Convert and print Lower case format, otherwise print “Inputted 
 Character is not A Alphabate”."""

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
op=input("Enter Arithmetic Operator: ")
if op=="+":
    print(x+y)
elif op=="-":
    print(x-y)
elif op=="*":
    print(x*y)
else:
    print("Invalid Arithmetic Operator")