"""(44) Write a program to enter Student Name and his three Subject Marks 
 then calculate Total and Average Marks and check if Average Marks 
 is greater than and equal to 60 then print Student Name and Grade-A
 else print Student Name and Grade-B. """
def student_marks():
    name = input("Enter the Student's Name: ")
    marks1 = int(input("Enter the first subject mark: "))
    marks2 = int(input("Enter the second subject mark: "))
    marks3 = int(input("Enter the third subject mark: "))
    t=marks1+marks2+marks3
    a=t/3
    if a>=60:
        print("Student Name ",name)
        print("Grade-A")
    else:
        print("Student Name ",name)
        print("Grade-B")
student_marks()
