"""(64) Write a program to enter any Number then print Digit of that Number 
 by using any Loop. (While/do-while/for) [Hints: n=54321 d=5]"""
n=int(input("Enter Number"))
i=0
while n!=0:
    n=n//10
    i=i+1
print(i)