"""(62) Write a program to print all ASCII Character of number from 1 to 255
 but skip the all Alphabate Characters (Capital & Small) using 
Continue statement."""
i=1
for i in range(1,255):
    if i >= 65 and i <= 90 or i >=97 and i <=122:
        continue
    print("%c"% (i))