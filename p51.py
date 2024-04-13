"""51) Write a program to enter Day Number then print appropriate Day, 
otherwise print Invalid Day Number. [Hints: 1-Sunday, 2-Monday, 3-Tue…]"""

day=int(input("Enter Day Number: "))
if(day==1):
    print("Sunday")
elif(day==2):
    print("Monday")
elif(day==3):
    print("Tuesday")
elif(day==4):
    print("Wednesday")
elif(day==5):
    print("Thursday")
elif(day==6):
    print("Friday")
else:
    print("Invalid Day Number")