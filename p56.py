"""(56) Write a program to print all Odd Numbers from 1 to 100. 
"""
i=100
while i>=1:
    if i % 2 ==1: #checking for odd numbers by using the modulus operator
        print(i, end=" ")
    i -= 1     #decrementing the value of 'i' after printing each