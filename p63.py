"""(63) Write a program to print all Alphabate Characters (Capital & small)
 using Continue statemen"""
i=64
for i in range(1,122):
    if i>=65 and i<=90:  # Capital alphabets
        print(chr(i),end=" ")
    elif i>=97 and i<=122:   # Small alphab
        print(chr(i), end = " ")