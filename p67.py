"""(67) Write a program to enter any Number then check inputted Number is 
Magic Number or not, if Number is Magic then print “Inputted 
Number is Magic No.” otherwise print “Inputted Number is not 
Magic No.” by using any Loop. [Hints: n=64 Digit of n is: 6+4=10]"""

n=int(input("Enter Any Number"))
x=n
r=0
while n!=0:
    b=n%10
    r=r+b
    n=n//10
if r==x:
    print("Magic Number", x)
else:
    print("Not Magic Number", x)