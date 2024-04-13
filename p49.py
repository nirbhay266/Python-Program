"""(49) Write a program to enter any Year then check inputted year is Leap 
 Year or Not. [Hints: if(y%4==0 & y%100!=0 | y%400==0) ]
LEAP YEAR RULES A year is a leap-year if it is evenly
divisible by 4 unless it is evenly divisible by 100, UNLESS it is
evenly divisible by 400. This means that 1800, 1900, and 2100 are
NOT leap years, but 2000 is a leap year, since it is evenly divisible
by 400!"""

y=int(input("Enter Year: "))
if(y%4==0 & y%100!=0 | y%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")