"""(45) Write a program to enter Student Name and his Six Subject Marks
then calculate Total Marks and Average Marks then check if Average 
Marks is greater than and equal to 60 then print Student Name and 
1st Division, if Average Marks is greater than and equal to 45 and 
less than 60 then print Student Name and 2nd Division, if Average 
Marks is greater than and equal to 30 and less than 45 then print 
Student Name and 3rd Division otherwise print Student Name and 
Fail. """
def student_info():
    name = input("Enter your name:")
    marks = []
    for i in range(6):
        mark = int(input(f"Enter your {i+1} subject mark:"))
        marks.append(mark)
    total = sum(marks)
    avg = total / len(marks)
    if avg >= 60:
        return f"{name}\n1st Division\nTotal Marks:{total}\nAverage Marks:{avg}"
    elif avg >= 45:
        return f"{name}\n2nd Division\nTotal Marks:{total}\nAverage Marks:{avg}"
    elif avg >= 30:
        return f"{name}\n3rd Division\nTotal Marks:{total}\nAverage Marks:{avg}"
    else:
        return f"{name}\nFail\nTotal Marks:{total}\nAverage Marks:{avg}"
print(student_info())
   

