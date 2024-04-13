"""(42) Write a program to enter Three Numbers then check largest one and 
 finally print largest one Number. If all inputted No. are Same then 
 print “All inputted No. are Same”. """

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
z=int(input("Enter Third Number: "))
if x>y and x>z:
    print("Largest Number is",x)
elif y>x and y>z:
    print("Largest Number is",y)
elif z>x and z>y:
        print("Largest Number is",z)
else:
        print("All inputted No. are Same")