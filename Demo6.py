def raam():
    n=int(input("Enter Any Number"))
    x=n
    r=0
    for i in range(n>0):
        b=n%10
        r=r*10+b
        n=n//10
    if r==x:
        print("Inputted Number is Palindrome")
    else:
        print("Inputted Number is not Palindrome")
       

raam()
