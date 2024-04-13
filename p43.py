"""(43) Write a program to enter Employee Name and its Basic Salary, if Basic 
Salary is greater than and equal to 3000 then give 10% TA and 5% 
HRA else give 20% DA and 10% HRA, finally calculate Net Salary
and finally print Employee Name and Net Salary. """

name=input("Enter Employee Name: ")
salary=int(input("Enter Employee Basic Salary: "))
if(salary>3000):
    ta=salary*0.1
    hra=salary*0.05
    net=salary+ta+hra
    print("Employee Name:",name,"\nNet Salary:",net)
else:
    da=salary*0.2
    hra=salary*.1
    net=salary+da+hra
    print("Employee Name:",name,"\nNet Salary:",net)