nm=input("Enter Name is")
m1=int(input("Student First Marks:"))
m2=int(input("Student Second Marks: "))
m3=int(input("Student Third Marks: "))
t=m1+m2+m3
a=float(t/3)
if a>60:
    print("Student Name is ",nm)
    print("Grade-A",a)
elif a>45 and a<60:
     print("Student Name is ",nm)
     print("Grade-B",a)
elif a>40 and a<45:
       print("Student Name is ",nm)
       print("Grade-c",a)
else:
     print("Sorry fail")
