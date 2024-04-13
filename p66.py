"""(66) Write a program to enter any Number then check inputted Number is 
Palindrome or Not, if Number is Palindrome then print “Inputted 
 Number is Palindrome” otherwise print “Inputted Number is not 
 Palindrome” by using any Loop. [Hints: n=121 r=121]"""
def is_palindrome():
    # Convert the number into string and check for palindrome
    n=int(input("Enter Any Number"))
    r=0
    x=n
    while n!=0:
        b=n%10
        r=r*10+b
        n=n//10
    if x==r:
        print("Inputted Number is Palindrome")
    else:
        print("Inputted Number is not Palindrome")
is_palindrome()