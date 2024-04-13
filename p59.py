"""(59) Write a program to enter any Number then print Table of that Number. 
"""
n=int(input("Enter Any Number"))
i=1
for i in range(1,11):
    print("%d x %d = %d"%(n,i,n*i))