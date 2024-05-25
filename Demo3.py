def is_P():
    n=int(input("Enter Any Numer"))
    x=n
    r=0
    while n!=0:
        b=n%10
        r=r*10+b
        n=n//10
    if x==r:
        print("Polindrom Number")
    else:
     print("Not Polindrom Number")
is_P()
