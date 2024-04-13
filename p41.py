"""(41) Write a program to enter Two Numbers then check largest one and 
 finally print largest one Number. If both are same then print All are 
 Same. """
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second number: "))
if(num1>num2):
    print("The Largest One is num1 ", num1)
elif(num2>num1):
    print("The Largest One is num2 ", num2)
else:
    if(num1==num2):
        print("All Are The Same")
   