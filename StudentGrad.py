nm = input("Student Name: ")
m1 = int(input("Student First Marks: "))
m2 = int(input("Student Second Marks: "))
m3 = int(input("Student Third Marks: "))
t = m1 + m2 + m3
a = float(t / 3)

if a >= 70:
    print(f"Grade: A, {nm}")
elif 70 > a > 50:
    print(f"Grade: B, {nm}")
elif 50 >= a > 30:
    print(f"Grade: C, {nm}")
