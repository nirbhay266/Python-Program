"""(65) Write a program to enter any Number then print Reverse of that 
 Number by using any Loop. [Hints: n=54321 d=12345]"""
n=int(input("Enter Any Number"))
r=0
while n!=0:
    d=n%10
    r=r*10+d
   # print(d,end="") 
    n//=10
print("\nReverse Of The Given Number Is :",r,end=" ")