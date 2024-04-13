"""(48) Write a program to enter any Name and Age then check if inputted 
 Age is less than 5 then print Child, if inputted Age is greater than and 
 equal to 5 and less than 18 then prints Teenager, if inputted Age is 
 greater than and equal to 18 and less than 30 then prints Young, if 
 inputted Age is greater than and equal to 30 then print OLD. """

def student_info():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    if(age<5):
        print("Child")
    elif(5<=age<=17):
        print("Teenager")
    elif(18<=age<30):
        print("Young")
    else:
        print("OLD")
        
student_info()